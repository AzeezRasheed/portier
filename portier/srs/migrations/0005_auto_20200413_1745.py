# Generated by Django 3.0.5 on 2020-04-13 17:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('srs', '0004_auto_20200413_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamkey',
            name='key',
            field=models.CharField(default=uuid.UUID('b5777854-4533-49dc-b38d-69738d8844d6'), max_length=64, unique=True),
        ),
    ]
