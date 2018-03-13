#!/usr/bin/env python3
import time

import bme680
import boto3


def put_data(name, value, room, timestamp):
    response = client.put_metric_data(
        Namespace='Home',
        MetricData=[
            {
                'MetricName': name,
                'Dimensions': [
                    {
                        'Name': 'Room',
                        'Value': room
                    },
                ],
                'Timestamp': timestamp,
                'Value': value,
                'Unit': 'None',
                'StorageResolution': 60
            },
        ]
    )


sensor = bme680.BME680()
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

timestamp = time.time()
client = boto3.client('cloudwatch')
put_data('Temperature', sensor.data.temperature, 'LivingRoom', timestamp)
put_data('Pressure', sensor.data.pressure, 'LivingRoom', timestamp)
put_data('Humidity', sensor.data.humidity, 'LivingRoom', timestamp)
