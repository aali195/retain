from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, PermissionDenied
from django.db.models import F
from django.shortcuts import get_object_or_404

from .serializers import (
    CollectionSerializer, 
    StatementSerializer, 
    UserSettingsSerializer, 
    UserSubscriptionsSerializer,
    CreatedCollectionSerializer,
    UpdateLearnedSerializer,
    UpdateReviewedSerializer
)

from .schedule import get_next_learn, get_next_review

from collecs.models import Collection
from statements.models import Statement
from usersettings.models import UserSettings
from subscriptions.models import Subscription
from progress.models import Progress


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

class LearnStatementView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = StatementSerializer

    def get_serializer_class(self): 
        serializer_class = self.serializer_class 
        if self.request.method == 'POST': 
            serializer_class = UpdateLearnedSerializer 
        return serializer_class

    def get_queryset(self):
        return get_next_learn(self.request.user)
        
    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)


class ReviewStatementView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

    def get_serializer_class(self): 
        serializer_class = self.serializer_class 
        if self.request.method == 'POST': 
            serializer_class = UpdateReviewedSerializer
        return serializer_class

    def list(self, request, *args, **kwargs):
        active_progress = get_next_review(self.request.user)

        user_settings = get_object_or_404(UserSettings, user=self.request.user)
        active_statements = Statement.objects.filter(collection=user_settings.active_collection)
        current_statement = get_object_or_404(active_statements, statement=active_progress.statement)
            
        other_statements = active_statements.exclude(statement=current_statement).order_by('?')[:3]

        return Response({
            'progress_id': active_progress.id,
            'statement_id': current_statement.id,
            'image': current_statement.image.path,
            'statement': current_statement.statement,
            'question': current_statement.question,
            'answer': current_statement.answer,
            'note': active_progress.note,
            'wrong_answer_1': other_statements[0].answer,
            'wrong_answer_2': other_statements[1].answer,
            'wrong_answer_3': other_statements[2].answer,
        })

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
