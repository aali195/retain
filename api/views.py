from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from .serializers import (
    CollectionSerializer, 
    StatementSerializer, 
    UserSettingsSerializer, 
    UserSubscriptionsSerializer,
    CreatedCollectionSerializer
)
from collecs.models import Collection
from statements.models import Statement
from usersettings.models import UserSettings
from subscriptions.models import Subscription


class ListCollectionsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Collection.objects.filter(is_visible=True).filter(size__gte=10)
    serializer_class = CollectionSerializer
    http_method_names = ['get']

    def get(self, request):
        collection = self.get_queryset()
        serializer = self.get_serializer_class()(collection)
        return Response(serializer.data)


class CreatedCollectionsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CollectionSerializer
    http_method_names = ['get']
    
    def get_queryset(self):
        return Collection.objects.filter(creator=self.request.user)
   

class StatementsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StatementSerializer

    def get_queryset(self):
        collection_id = self.kwargs['collection_id']
        if not Collection.objects.filter(pk=collection_id, is_visible=True).exists():
            raise NotFound(detail="Not found.", code=404)
        else:
            return Statement.objects.filter(collection_id=collection_id)
        
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserSettingsView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSettingsSerializer

    def get_queryset(self):
        return UserSettings.objects.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class UserSubscriptionsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSubscriptionsSerializer

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)