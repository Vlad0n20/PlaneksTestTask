# Generated by Django 4.2 on 2024-01-20 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schemas', to=settings.AUTH_USER_MODEL),
        ),
    ]
