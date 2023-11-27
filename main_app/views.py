from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_jwt.utils import jwt_decode_handler

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

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_clases = [permissions.IsAuthenticated]

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

class GoalCreate(generics.CreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user_id = decode_token(request)  # Use the decode_token function
        if user_id:
            request.data['user'] = user_id  # Associate user ID with the goal
            return super().create(request, *args, **kwargs)
        else:
            return Response({'detail': 'Invalid or missing token'}, status=status.HTTP_401_UNAUTHORIZED)

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

class HabitCreate(generics.CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = GoalSerializer

class CompletedHabitViewSet(viewsets.ModelViewSet):
    queryset = CompletedHabit.objects.all()
    serializer_class = CompletedHabitSerializer
    permission_classes = [permissions.IsAuthenticated]

def decode_token(request):
    authorization_header = request.headers.get('Authorization')
    if authorization_header:
        token = authorization_header.split(' ')[1]
        decoded_token = jwt_decode_handler(token)
        user_id = decoded_token['user_id']
        return user_id
    return None
