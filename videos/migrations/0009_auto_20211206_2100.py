# Generated by Django 3.2.9 on 2021-12-06 21:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_video_publish_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
