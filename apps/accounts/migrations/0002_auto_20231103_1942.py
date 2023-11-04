# Generated by Django 3.2.22 on 2023-11-04 02:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dd51d222-e292-4af3-9144-3c3ed1129679'), primary_key=True, serialize=False, unique=True),
        ),
    ]
