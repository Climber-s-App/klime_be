from rest_framework import serializers
from .models import User, Wall, Problem
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = ["id", "name", "photo_url", "user_id"]
class WallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = ["id", "name", "photo_url", "user_id"]
class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ["id", "name", "vectors", "wall_id"]

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     vectors_data = instance.object.vectors.all()  # Replace this with your actual logic to fetch vectors data

    #     vectors_representation = []
    #     for vector in vectors_data:
    #         vector_representation = {
    #             "id": vector.id,  # Include the id field
    #             "x": vector.x,    # Include other fields as needed
    #             "y": vector.y,
    #             "z": vector.z,
    #         }
    #         vectors_representation.append(vector_representation)

    #     representation["vectors"] = vectors_representation
    #     return representation

        # representation = super().to_representation(instance)
        # new_representation = {
        #     'id': representation.get('id'),
        #     'type': 'library',
        #     'attributes': {
        #         'name': representation.get('name'),
        #         'address': {
        #             'street': representation.get('street'),
        #             'city': representation.get('city'),
        #             'state': representation.get('state'),
        #             'zip': representation.get('zip'),
        #         },
        #         'location': {
        #             'lat': representation.get('lat'),
        #             'lon': representation.get('lon'),
        #         },
        #         'book_count': instance.book_set.count(),
        #     }
        # }
        # return new_representation
