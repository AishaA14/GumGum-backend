# Generated by Django 4.2.7 on 2023-11-24 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_habit_last_completed_alter_habit_goal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='timeframe',
            new_name='goal_duration',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='frequency_amount',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='frequency_unit',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='last_completed',
        ),
        migrations.CreateModel(
            name='CompletedHabit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('count', models.IntegerField()),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.habit')),
            ],
        ),
    ]