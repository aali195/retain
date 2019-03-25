from rest_framework import serializers

from collecs.models import Collection
from statements.models import Statement
from usersettings.models import UserSettings


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

class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = (
            'user',
            'active_collection',
            'review_num',
        )
        read_only_fields = ('user',)

        def update(self, instance, validated_data):
            instance.active_collection = validated_data.get('active_collection', instance.active_collection)
            instance.review_num(validated_data.get('review_num', instance.review_num))
            instance.save()
            return instance