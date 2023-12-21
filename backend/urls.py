"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from main_app import views
from main_app.views import HabitListCreateView, HabitDetailViewSet, CompletedHabitViewSet, CompletedHabitListCreateView


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'goal', views.GoalViewSet)
router.register(r'task', views.TaskViewSet)
router.register(r'habit', views.HabitDetailViewSet)
router.register(r'completed_habits', CompletedHabitViewSet, basename='completed_habits')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),

    path('goal/<int:pk>/', views.GoalViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='goal_detail'),
    path('goal/create/', views.GoalCreate.as_view(), name='goal_create'),

    path('task/<int:pk>/', views.TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='task_detail'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    
    path('habits/goal/<int:goal_id>/', HabitListCreateView.as_view(), name='habit-list-create'),
    path('habits/<int:pk>/', HabitDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='habit-detail'),

    path('completed_habit/habit/<int:habit_id>/', CompletedHabitListCreateView.as_view(), name='completed_habit_create'),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]