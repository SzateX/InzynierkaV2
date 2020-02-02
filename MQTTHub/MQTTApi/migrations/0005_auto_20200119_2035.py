# Generated by Django 2.2.7 on 2020-01-19 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MQTTApi', '0004_auto_20191215_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceunit',
            name='type_of_unit',
            field=models.CharField(choices=[('humidity', 'Humidity Unit'), ('temperature', 'Temperature Unit'), ('switch', 'Switch Unit'), ('unknown', 'Unknown Unit')], max_length=200),
        ),
        migrations.CreateModel(
            name='UnknownUnitValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('incoming', models.BooleanField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(blank=True, max_length=200, null=True)),
                ('device_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MQTTApi.DeviceUnit')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
