# Generated by Django 4.1.7 on 2023-03-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_remove_docs_files_docs_files_cl_docs_files_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='first_name',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='docs',
            name='last_name',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
