# Generated by Django 3.0 on 2019-12-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]