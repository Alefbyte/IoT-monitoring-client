# Temp.py

from ds18b20 import DS18B20
import requests
import time
import os
from datetime import datetime

# test temperature sensors
x = DS18B20()
count = x.device_count()
i = 0

while (True):
    time.sleep(5)
    while i < count:
        uuid = x.read_name(i)
        temp = x.tempC(i)

        response = requests.post("{url}/api/metrics/logs".format(url=os.environ.get('DJANGO_URL')),
                                 data={
                                     'logged_at': datetime.now(),
                                     'temp': temp,
                                     'uuid': uuid
                                 })
        print(response.json())

        print("ID:  {id} --> temperature:  {temp}".format(id=uuid, temp=temp))
        i += 1
