from rest_framework import serializers

from collecs.models import Collection

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = (
            'id',
            'title', 
            'image', 
            'description', 
            'size', 
            'upload_date',
            'last_update',
            'rating',
        )