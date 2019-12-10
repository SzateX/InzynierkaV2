# Generated by Django 2.2.7 on 2019-12-10 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MQTTApi', '0002_deviceunit_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectedUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_hub', models.IntegerField()),
                ('to_device', models.IntegerField()),
                ('to_unit', models.IntegerField()),
                ('from_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MQTTApi.DeviceUnit')),
            ],
        ),
    ]
