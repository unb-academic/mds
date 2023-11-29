# Generated by Django 4.2.7 on 2023-11-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submissions", "0002_alter_submission_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="submission",
            name="status",
            field=models.TextField(
                choices=[
                    ("WJ", "Waiting judge"),
                    ("JG", "Judging"),
                    ("AC", "Accepted"),
                    ("WA", "Wrong answer"),
                    ("RE", "Runtime error"),
                    ("TLE", "Time limit exceeded"),
                    ("MLE", "Memory limit exceeded"),
                    ("CE", "Compilation error"),
                    ("IE", "Internal error"),
                    ("UE", "Unknown error"),
                    ("SE", "Submission error"),
                    ("PE", "Presentation error"),
                ],
                default="WJ",
                max_length=3,
            ),
        ),
    ]
