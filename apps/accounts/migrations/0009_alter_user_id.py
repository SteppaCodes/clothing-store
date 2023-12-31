# Generated by Django 4.2.6 on 2023-12-08 18:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("0eab44d4-c0e2-4c8d-a416-0cc152bff70b"),
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
