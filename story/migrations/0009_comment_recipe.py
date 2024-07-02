# Generated by Django 4.0.10 on 2024-06-30 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0008_remove_comment_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_comment', to='story.recipes'),
        ),
    ]
