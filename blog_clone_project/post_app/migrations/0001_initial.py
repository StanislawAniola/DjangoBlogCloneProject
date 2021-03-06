# Generated by Django 2.2.9 on 2020-02-03 18:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group_app', '0002_auto_20200203_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_author', models.TextField(max_length=264)),
                ('post_text', models.TextField(max_length=264)),
                ('post_creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_approved', models.BooleanField(default=False)),
                ('post_belong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_belong_to_group', to='group_app.GroupModel')),
            ],
        ),
    ]
