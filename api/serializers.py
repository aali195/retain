from rest_framework import serializers

from collecs.models import Collection
from statements.models import Statement


class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = (
            'id',
            'collection',
            'image',
            'statement', 
            'question', 
            'answer',
        )
    
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = (
            'id',
            'title',
            'creator',
            'image', 
            'description', 
            'size', 
            'upload_date',
            'last_update',
            'rating',
        )