# Generated by Django 3.0 on 2019-12-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20191220_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default='king fahad road', max_length=255),
            preserve_default=False,
        ),
    ]
