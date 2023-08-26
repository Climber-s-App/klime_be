#imports
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer

def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({"data": serializer.data}, safe=False)