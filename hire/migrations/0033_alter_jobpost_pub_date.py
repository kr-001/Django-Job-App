# Generated by Django 4.1.1 on 2023-03-03 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0032_alter_jobpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 3, 3, 11, 36, 12, 929566)),
        ),
    ]
