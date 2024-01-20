# Generated by Django 4.2 on 2024-01-20 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('column', '0001_initial'),
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='schema',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='columns', to='schema.schema', verbose_name='Schema'),
        ),
    ]