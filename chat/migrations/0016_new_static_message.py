# Generated by Django 4.1.1 on 2023-05-19 15:06

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0015_static_message_delete_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_Static_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=20, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('company_name', models.TextField(blank=True, null=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('perant_id', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='chat.new_static_message')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]