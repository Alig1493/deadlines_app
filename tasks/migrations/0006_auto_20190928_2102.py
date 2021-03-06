# Generated by Django 2.2.5 on 2019-09-29 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0005_remove_task_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='students',
        ),
        migrations.CreateModel(
            name='StudentHasTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Task', to='tasks.Task')),
            ],
        ),
    ]
