# Generated by Django 3.2.8 on 2021-10-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_submission', '0002_rename_story_submission_storysubmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='storysubmission',
            name='approved_story',
            field=models.BooleanField(default=False),
        ),
    ]
