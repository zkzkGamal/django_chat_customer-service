# Generated by Django 4.1.1 on 2023-05-17 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0013_job_perant_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='message_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]