from rest_framework import serializers
from . import models

class Serialiaze_M(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['title','body']