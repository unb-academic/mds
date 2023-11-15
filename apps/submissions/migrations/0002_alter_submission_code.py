# Generated by Django 4.2.7 on 2023-11-15 12:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submissions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="code",
            field=models.TextField(
                validators=[django.core.validators.MinLengthValidator(15)]
            ),
        ),
    ]
