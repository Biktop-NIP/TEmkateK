# Generated by Django 4.2.4 on 2023-08-18 12:48

from django.db import migrations, models
import videos.models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_tag_tag_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=videos.models.update_filename),
        ),
    ]
