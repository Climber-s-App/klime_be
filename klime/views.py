#imports
from django.http import JsonResponse
from .models import User, Wall, Problem
from .serializers import UserSerializer, WallSerializer, ProblemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse({"data": serializer.data}, safe=False)

def user_details(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        serializer = UserSerializer(user, many=False)
        return JsonResponse({"data": serializer.data}, safe=False)
    except User.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['GET, POST'])
def get_user_walls(request, user_id):
    user = User.objects.get(pk=user_id)
    walls = user.wall_set
    serializer = WallSerializer(walls, many=True)
    return JsonResponse({"data": serializer.data}, safe=False)

    # if request.method == "POST":
    #     user = User.objects.get(pk=user_id)
    #     walls = user.wall_set
    #     serializer = WallSerializer(walls, many=True)
    #     return JsonResponse({"data": serializer.data}, safe=False)

def get_user_wall_details(request, user_id, wall_id):
    user = User.objects.get(pk=user_id)
    wall = user.wall_set.get(pk=wall_id)
    serializer = WallSerializer(wall, many=False)
    return JsonResponse({"data": serializer.data}, safe=False)

@api_view(['GET', 'POST'])
def get_wall_problems(request, user_id, wall_id):
    if request.method == 'GET':
        user = User.objects.get(pk=user_id)
        wall = user.wall_set.get(pk=wall_id)
        problem = wall.problem_set
        serializer = ProblemSerializer(problem, many=True)
        return JsonResponse({"data": serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  # Return errors in response

def get_wall_problem_details(request, user_id, wall_id, problem_id):
    user = User.objects.get(pk=user_id)
    wall = user.wall_set.get(pk=wall_id)
    problem = wall.problem_set.get(pk=problem_id)
    serializer = ProblemSerializer(problem, many=False)
