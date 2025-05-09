# Generated by Django 5.2 on 2025-05-05 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customPrebuilts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gamespec",
            name="geforce_card_id",
        ),
        migrations.RemoveField(
            model_name="gamespec",
            name="radeon_card_id",
        ),
        migrations.AddField(
            model_name="gamespec",
            name="geforce_card",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="customPrebuilts.partsgpu",
            ),
        ),
    ]
