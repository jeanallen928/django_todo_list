from rest_framework import serializers
from todos.models import Todo
from django.utils import timezone


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Todo
        fields = "__all__"


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title", "is_complete", "completion_at", "completed_at")

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.is_complete = validated_data.get(
            "is_complete", instance.is_complete)
        instance.completion_at = validated_data.get(
            "completion_at", instance.completion_at)
        if instance.is_complete is True:
            instance.completed_at = timezone.now()
        else:
            instance.completed_at = None
        instance.save()
        return instance
