# Generated by Django 3.2.3 on 2021-05-31 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210531_0736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogposts',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]
