import os # environ variables
import uuid # unique id for each image
import boto3 # amazon bucket for the images
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class HomeView(APIView):
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)

class LogoutView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_clases = [permissions.IsAuthenticated]

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Goal.objects.filter(user=request.user)
        serializer = GoalSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = GoalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Goal.objects.filter(user=request.user, pk=pk)
        goal = get_object_or_404(queryset, pk=pk)
        serializer = GoalSerializer(goal)
        return Response(serializer.data)

    def update(self, request, pk=None):
        goal = Goal.objects.get(pk=pk)
        serializer = GoalSerializer(goal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        goal = Goal.objects.get(pk=pk)
        goal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Habit.objects.filter(user=request.user)
        serializer = HabitSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = HabitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Habit.objects.filter(user=request.user, pk=pk)
        habit = get_object_or_404(queryset, pk=pk)
        serializer = HabitSerializer(habit)
        return Response(serializer.data)

    def update(self, request, pk=None):
        habit = Habit.objects.get(pk=pk)
        serializer = HabitSerializer(habit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        habit = Habit.objects.get(pk=pk)
        habit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CompletedGoalViewSet(viewsets.ModelViewSet):
    queryset = CompletedGoal.objects.all()
    serializer_class = CompletedGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

class CompletedHabitViewSet(viewsets.ModelViewSet):
    queryset = CompletedHabit.objects.all()
    serializer_class = CompletedHabitSerializer
    permission_classes = [permissions.IsAuthenticated]




