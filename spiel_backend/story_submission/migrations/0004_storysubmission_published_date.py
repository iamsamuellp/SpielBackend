# Generated by Django 3.2.8 on 2021-10-13 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story_submission', '0003_storysubmission_approved_story'),
    ]

    operations = [
        migrations.AddField(
            model_name='storysubmission',
            name='published_date',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Creation date'),
        ),
    ]
