from learn_signals import models
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = "__all__"