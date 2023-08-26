from rest_framework import serializers
from .models import User, Wall

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = ["id", "name", "photo_url", "user_id"]
