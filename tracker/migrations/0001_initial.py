# Generated by Django 2.1 on 2018-08-24 15:53

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_hours', models.SmallIntegerField(default=0)),
                ('time_minutes', models.IntegerField(default=0)),
                ('task_performed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Task')),
            ],
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_text', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='performed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Username'),
        ),
    ]