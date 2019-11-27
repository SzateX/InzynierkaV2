from django.db import models

from MQTTApi.enums import TemperatureUnit, \
    HumidityUnit, DeviceType, UnitDirection, UnitType


class Device(models.Model):
    __TYPE_CHOICES = (
        (DeviceType.GENERIC_TEMPERATURE_SENSOR, 'Generic Temperature Sensor'),
        (DeviceType.GENERIC_HUMIDITY_SENSOR, 'Generic Humidity Sensor'),
        (DeviceType.GENERIC_LAMP, 'GL')
    )
    name = models.CharField(max_length=200)
    type_of_device = models.CharField(choices=__TYPE_CHOICES, max_length=200)


class DeviceUnit(models.Model):
    __DIRECTION_CHOICES = (
        (UnitDirection.INPUT, 'input'),
        (UnitDirection.OUTPUT, 'output'),
        (UnitDirection.IN_OUT, 'input/output')
    )
    __TYPE_CHOICES = (
        (UnitType.HUMIDITY_UNIT, 'Humidity Unit'),
        (UnitType.TEMPERATURE_UNIT, 'Temperature Unit'),
        (UnitType.SWITCH_UNIT, 'Switch Unit')
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE,
                               related_name='units',
                               max_length=200)
    direction = models.CharField(choices=__DIRECTION_CHOICES, max_length=200)
    type_of_unit = models.CharField(choices=__TYPE_CHOICES, max_length=200)


class GenericUnitValue(models.Model):
    device_unit = models.ForeignKey(DeviceUnit, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    incoming = models.BooleanField()

    class Meta:
        abstract = True


class SwitchUnitValue(GenericUnitValue):
    value = models.BooleanField()


class TemperatureUnitValue(GenericUnitValue):
    __UNIT_CHOICES = (
        (TemperatureUnit.CELSIUS, 'C'),
        (TemperatureUnit.KELVIN, 'K'),
        (TemperatureUnit.FAHRENHEIT, 'F')
    )
    value = models.DecimalField(decimal_places=2, max_digits=10)
    unit = models.CharField(choices=__UNIT_CHOICES, max_length=200)


class HumidityUnitValue(GenericUnitValue):
    __UNIT_CHOICES = (
        (HumidityUnit.PERCENTAGE, '%'),
        (HumidityUnit.GRAMS_PER_METER_SQUARED, 'g/m**3')
    )
    value = models.DecimalField(decimal_places=2, max_digits=10)
    unit = models.CharField(choices=__UNIT_CHOICES,
                            max_length=200)