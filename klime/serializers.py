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
class WallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = ["id", "name", "photo_url", "user_id"]
# class ProblemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Problem
#         fields = ["id", "name", "vectors", "wall_id"]

class VectorSerializer(serializers.ModelSerializer):
    color = serializers.CharField()
    id = serializers.CharField()
    initialX = serializers.FloatField()
    initialY = serializers.FloatField()
    x = serializers.FloatField()
    y = serializers.FloatField()
class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        new_representation = {
            "id": representation.get('id'),
            "type": "problem",
            "attributes": {
                "name": representation.get('name'),
                "vectors": [
                    {
                        "color": vector.get('color'),
                        "id": vector.get('id'),
                        "initialX": vector.get('initialX'),
                        "initialY": vector.get('initialY')
                    }
                    for vector in representation.get('vectors', [])
                ],
                "wall_id": representation.get('wall_id'),
                "grade": representation.get('grade')
        }
    }
        return new_representation

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
