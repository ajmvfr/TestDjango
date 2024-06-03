# Generated by Django 5.0.6 on 2024-05-31 01:46

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('publish_date', models.DateField(default=datetime.date.today)),
                ('expire_date', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('sort_order', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]