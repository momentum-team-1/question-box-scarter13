# Generated by Django 3.0.7 on 2020-06-21 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_answer_correct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['date']},
        ),
    ]
