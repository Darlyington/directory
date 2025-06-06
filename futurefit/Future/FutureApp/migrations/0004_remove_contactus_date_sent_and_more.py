# Generated by Django 5.2 on 2025-05-21 10:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FutureApp', '0003_store'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='date_sent',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='subject',
        ),
        migrations.AddField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contactus',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
