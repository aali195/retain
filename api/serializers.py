from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.shortcuts import get_object_or_404

from collecs.models import Collection
from statements.models import Statement
from usersettings.models import UserSettings
from subscriptions.models import Subscription
from progress.models import Progress


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
        read_only_fields = ('id', 'image',)

    def validate(self, data):
        data = super(StatementSerializer, self).validate(data)
        collection = data['collection']
        if not Collection.objects.filter(creator=self.context['request'].user, id=collection.id).exists():
            raise serializers.ValidationError("User not collection creator")
        return data

    def create(self, validated_data):
        validated_data.pop('user', None)
        return Statement.objects.create(**validated_data)
    

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

class CreatedCollectionSerializer(serializers.ModelSerializer):
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


class UpdateLearnedSerializer(serializers.Serializer):
    note = serializers.CharField(max_length=250, default='N/A')
    statement_id = serializers.IntegerField()

    def validate(self, data):
        data = super(UpdateLearnedSerializer, self).validate(data)
        statement = get_object_or_404(Statement, pk=data['statement_id'])
        user_settings = get_object_or_404(UserSettings, user=self.context['request'].user)

        if statement.collection != user_settings.active_collection:
            raise serializers.ValidationError("Statement collection is not active")
        else:
            if not Progress.objects.filter(user=self.context['request'].user, statement=statement).exists():
                return data
            else:
                raise serializers.ValidationError("Statement has already been learned")


    def create(self, validated_data):
        statement = get_object_or_404(Statement, pk=validated_data['statement_id'])
        subscription = get_object_or_404(Subscription, user=self.context['request'].user, collection=statement.collection)
        subscription.completed_count += 1
        subscription.save()
        return Progress.objects.create(user=self.context['request'].user, statement=statement, note=validated_data['note'])


