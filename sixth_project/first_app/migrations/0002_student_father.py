# Generated by Django 5.0.6 on 2024-06-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father',
            field=models.TextField(default='rahim'),
        ),
    ]
