# Generated by Django 3.0.5 on 2020-09-10 18:47

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=12)),
                ('sms_body', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
            managers=[
                ('valid_sms', django.db.models.manager.Manager()),
            ],
        ),
    ]
