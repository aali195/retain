from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

from .serializers import CollectionSerializer, StatementSerializer
from collecs.models import Collection
from statements.models import Statement

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