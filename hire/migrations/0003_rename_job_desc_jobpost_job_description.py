# Generated by Django 4.1.7 on 2023-03-02 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0002_jobpost_job_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='job_desc',
            new_name='job_description',
        ),
    ]
