# Generated by Django 3.2.7 on 2021-10-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='image',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='resume',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
