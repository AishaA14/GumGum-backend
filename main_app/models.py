from django.db import models
from django.contrib.auth.models import User

# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=255)
#     email = models.EmailField()

# class Tag(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    # photo = models.ImageField(upload_to='goal_photos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    # tag = models.ManyToManyField(Tag)
    timeframe = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    completed = models.BooleanField(default=False)

class Habit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    frequency_unit_choices = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]
    frequency_unit = models.CharField(max_length=10, choices=frequency_unit_choices,  default='daily')
    frequency_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, default=2)

# class CompletedGoal(models.Model):
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
#     completed = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)

class CompletedHabit(models.Model):
    id = models.AutoField(primary_key=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)