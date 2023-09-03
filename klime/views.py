#imports
from django.http import JsonResponse
from .models import User, Wall, Problem
from .serializers import UserSerializer, WallSerializer, ProblemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse({"data": serializer.data}, safe=False)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, user_id):
    try:
        user = User.objects.get(pk=user_id)

        if request.method == 'GET':
            user = User.objects.get(pk=user_id)
            serializer = UserSerializer(user, many=False)
            return JsonResponse({"data": serializer.data}, safe=False)

        elif request.method == 'PUT':
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"data": serializer.data}, safe=False)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def user_walls(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        walls = user.wall_set.all()
        serializer = WallSerializer(walls, many=True)
        return JsonResponse({"data": serializer.data}, safe=False)

    elif request.method == 'POST':
        serializer = WallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({"message": "Wall created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_user_wall_details(request, user_id, wall_id):
    user = User.objects.get(pk=user_id)
    wall = user.wall_set.get(pk=wall_id)
    serializer = WallSerializer(wall, many=False)
    return JsonResponse({"data": serializer.data}, safe=False)

@api_view(['GET', 'POST'])
def get_wall_problems(request, user_id, wall_id_id):
    if request.method == 'GET':
        user = User.objects.get(pk=user_id)
        wall = user.wall_set.get(pk=wall_id_id)
        problem = wall.problem_set
        serializer = ProblemSerializer(problem, many=True)
        return JsonResponse({"data": serializer.data}, safe=False)

    if request.method == 'POST':
        user = User.objects.get(pk=user_id)
        wall = user.wall_set.get(pk=wall_id_id)
        serializer = ProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Problem created successfully"}, status=status.HTTP_201_CREATED)
        return JsonResponse({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  # Return errors in response

def get_wall_problem_details(request, user_id, wall_id, problem_id):
    user = User.objects.get(pk=user_id)
    wall = user.wall_set.get(pk=wall_id)
    problem = wall.problem_set.get(pk=problem_id)
    serializer = ProblemSerializer(problem, many=False)
    return JsonResponse({"data": serializer.data}, safe=False)
