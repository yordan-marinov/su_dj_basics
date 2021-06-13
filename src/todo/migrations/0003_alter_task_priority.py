# Generated by Django 3.2.3 on 2021-06-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('3', 'High'), ('2', 'Medium'), ('1', 'Low')], max_length=6),
        ),
    ]
