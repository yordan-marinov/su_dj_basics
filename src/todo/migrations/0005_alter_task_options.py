# Generated by Django 3.2.3 on 2021-06-14 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_task_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['complete', '-priority']},
        ),
    ]
