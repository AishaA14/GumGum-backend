import os # environ variables
import uuid # unique id for each image
import boto3 # amazon bucket for the images
from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
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
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

class GoalCreate(generics.CreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        goal_id = self.kwargs['goal_id']
        return Habit.objects.filter(goal_id=goal_id)

    def perform_create(self, serializer):
        goal_id = self.kwargs['goal_id']
        goal = Goal.objects.get(pk=goal_id)
        serializer.save(goal=goal)

    def put(self, serializer, pk):
        habit = self.get_object(pk=pk)
        return habit

class CompletedHabitListCreateView(generics.ListCreateAPIView):
    serializer_class = CompletedHabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        habit_id = self.kwargs['habit_id']
        return CompletedHabit.objects.filter(habit_id=habit_id)

    def perform_create(self, serializer):
        habit_id = self.kwargs['habit_id']
        habit = Habit.objects.get(pk=habit_id)
        serializer.save(habit=habit)

    def put(self, serializer, pk):
        completed_habit = self.get_object(pk=pk)
        return completed_habit
    
class HabitDetailViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompletedHabitViewSet(viewsets.ModelViewSet):
    queryset = CompletedHabit.objects.all()
    serializer_class = CompletedHabitSerializer
    permission_classes = [permissions.IsAuthenticated]


