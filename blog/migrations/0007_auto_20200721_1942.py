# Generated by Django 2.2 on 2020-07-21 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200720_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
