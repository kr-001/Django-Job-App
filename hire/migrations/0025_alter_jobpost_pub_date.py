# Generated by Django 4.1.7 on 2023-03-03 05:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0024_alter_jobpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 3, 3, 11, 8, 5, 546384)),
        ),
    ]
