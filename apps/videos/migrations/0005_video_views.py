# Generated by Django 4.2.4 on 2023-08-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_video_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='просмотры'),
        ),
    ]
