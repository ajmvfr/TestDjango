# Generated by Django 5.0.6 on 2024-06-02 21:11

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_announcement_media_field_alter_announcement_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='media_field',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
