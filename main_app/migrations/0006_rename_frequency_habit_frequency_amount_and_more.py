# Generated by Django 4.2.7 on 2023-11-22 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_goal_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='habit',
            old_name='frequency',
            new_name='frequency_amount',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='user',
        ),
        migrations.AddField(
            model_name='habit',
            name='frequency_unit',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], default='daily', max_length=10),
        ),
        migrations.AddField(
            model_name='habit',
            name='goal',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.goal'),
        ),
    ]
