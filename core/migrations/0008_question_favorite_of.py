# Generated by Django 3.0.7 on 2020-06-22 00:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0007_auto_20200621_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='favorite_of',
            field=models.ManyToManyField(related_name='favorite_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
