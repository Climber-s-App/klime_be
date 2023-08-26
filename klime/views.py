#imports
from django.http import JsonResponse
from .models import User, Wall, Problem
from .serializers import UserSerializer, WallSerializer, ProblemSerializer

def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({"data": serializer.data}, safe=False)

def wall_list(request):
    walls = Wall.objects.all()
    serializer = WallSerializer(walls, many=True)
    return JsonResponse({"data": serializer.data}, safe=False)

def problem_list(request):
    problems = Problem.objects.all()
    serializer = ProblemSerializer(problems, many=True)
    return JsonResponse({"data": serializer.data}, safe=False)