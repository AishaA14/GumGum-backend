from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    goal_duration = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

class Habit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, default=None)
    is_completed = models.BooleanField(default=False)

class CompletedHabit(models.Model):
    id = models.AutoField(primary_key=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()

class Task(models.Model):
    completed_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)