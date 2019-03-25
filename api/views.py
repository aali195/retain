from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from .serializers import CollectionSerializer, StatementSerializer, UserSettingsSerializer
from collecs.models import Collection
from statements.models import Statement
from usersettings.models import UserSettings

class ListCollectionsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    http_method_names = ['get']

    def get(self, request):
        collection = self.get_queryset()
        serializer = self.get_serializer_class()(collection)
        return Response(serializer.data)
        

class GetStatementsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StatementSerializer
    http_method_names = ['get']

    def get_queryset(self):
        collection_id = self.kwargs['collection_id']
        statement = Statement.objects.filter(collection_id=collection_id)
        if statement:
            return statement
        else:
            raise NotFound(detail="Not found.", code=404)

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