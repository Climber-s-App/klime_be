from rest_framework import serializers
from .models import User, Wall, Problem
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = ["id", "name", "photo_url", "user"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        new_representation = {
            "id": representation.get('id'),
            "type": "wall",
            "attributes": {
                "name": representation.get("name"),
                "photo_url": representation.get("photo_url"),
                "user_id": representation.get("user")
            }
        }
        return new_representation
class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ["id", "name", "vectors", "grade", "wall"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        new_representation = {
            "id": representation.get('id'),
            "type": "problem",
            "attributes": {
                "name": representation.get('name'),
                "vectors": representation.get('vectors'),
                "wall_id": representation.get('wall'),
                "grade": representation.get('grade')
        }
    }
        return new_representation
