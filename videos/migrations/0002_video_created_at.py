# Generated by Django 3.2.25 on 2024-10-16 10:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_create_video_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]