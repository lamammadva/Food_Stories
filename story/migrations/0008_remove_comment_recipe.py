# Generated by Django 4.0.10 on 2024-06-30 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_remove_recipes_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recipe',
        ),
    ]
