from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from collecs.models import Collection
from statements.models import Statement
from usersettings.models import UserSettings
from subscriptions.models import Subscription


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
            'active_sub',
            'review_num',
        )
        read_only_fields = ('user',)

        def update(self, instance, validated_data):
            instance.active_sub = validated_data.get('active_sub', instance.active_sub)
            instance.review_num(validated_data.get('review_num', instance.review_num))
            instance.save()
            return instance


class UserSubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'user',
            'collection',
            'sub_date',
            'completed_count',
            'rating',
        )
        read_only_fields = ('user', 'sub_date', 'completed_count', 'rating')