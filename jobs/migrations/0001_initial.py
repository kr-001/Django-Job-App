# Generated by Django 4.1.1 on 2023-03-03 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hire', '0033_alter_jobpost_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='docs',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('files', models.FileField(default=None, max_length=250, null=True, upload_to='jobs/file/')),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hire.jobpost', verbose_name='Foreign Key')),
            ],
        ),
    ]
