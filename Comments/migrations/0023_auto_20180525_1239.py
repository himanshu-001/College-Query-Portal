# Generated by Django 2.0.5 on 2018-05-25 07:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Comments', '0022_auto_20180520_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]