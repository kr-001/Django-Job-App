# Generated by Django 4.1.7 on 2023-03-02 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0005_alter_jobpost_job_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 3, 2, 17, 27, 3, 910372)),
        ),
    ]
