# Generated by Django 2.2.7 on 2019-12-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MQTTApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceunit',
            name='name',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]