# Generated by Django 2.2.7 on 2020-02-05 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_title', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=1000)),
                ('end_date', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=1000)),
                ('task_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Task')),
            ],
        ),
    ]
