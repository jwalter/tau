# Generated by Django 3.1.7 on 2021-04-09 01:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Streamer',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('twitch_username', models.CharField(max_length=64)),
                ('twitch_id', models.CharField(blank=True, max_length=64, null=True)),
                ('streaming', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
