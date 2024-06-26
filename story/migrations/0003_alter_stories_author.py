# Generated by Django 4.0.10 on 2024-06-15 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('story', '0002_remove_stories_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='story_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
