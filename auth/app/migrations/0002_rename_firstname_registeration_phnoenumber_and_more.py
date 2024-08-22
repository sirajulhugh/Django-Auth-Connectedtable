# Generated by Django 5.0.7 on 2024-07-17 05:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeration',
            old_name='firstname',
            new_name='phnoenumber',
        ),
        migrations.RemoveField(
            model_name='registeration',
            name='dateofjoin',
        ),
        migrations.RemoveField(
            model_name='registeration',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='registeration',
            name='role',
        ),
        migrations.AddField(
            model_name='registeration',
            name='images',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='registeration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]