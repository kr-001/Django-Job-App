# Generated by Django 4.1.7 on 2023-03-03 17:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hire', '0034_alter_jobpost_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 3, 3, 22, 41, 59, 165843)),
        ),
        migrations.CreateModel(
            name='accepted',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default=None, max_length=50)),
                ('name', models.CharField(default=None, max_length=50, null=True)),
                ('resume', models.FileField(default=None, max_length=50, upload_to='jobs/accepted/resumes')),
                ('coverLetter', models.FileField(default=None, max_length=50, upload_to='jobs/accepted/covers')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hire.jobpost')),
            ],
        ),
    ]