# Generated by Django 3.0 on 2019-12-26 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_event_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(default='mm', upload_to='image/'),
        ),
    ]