# Generated by Django 2.2.9 on 2020-02-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_app', '0002_auto_20200203_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmodel',
            name='group_title',
            field=models.CharField(max_length=264),
        ),
    ]
