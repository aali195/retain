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
            'active_collection',
            'review_num',
        )
        read_only_fields = ('user',)

    def validate(self, data):
        data = super(UserSettingsSerializer, self).validate(data)
        collection = data['active_collection']
        if not Subscription.objects.filter(user=self.context['request'].user, collection=collection).exists():
            raise serializers.ValidationError("User not subscribed to collection")
        return data


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
    
    def validate(self, data):
        data = super(UserSubscriptionsSerializer, self).validate(data)
        collection = data['collection']
        if not Subscription.objects.filter(user=self.context['request'].user, collection=collection).exists():
            return data
        raise serializers.ValidationError("Duplicate subscription")