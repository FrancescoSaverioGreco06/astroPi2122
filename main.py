import functions

if __name__ == '__main__':
    print('main.py - AstroPI 2021/2022')

from Test import csv_creator
from Test import capture
from Test import day_night
from Test import ndvi
from time import sleep
from datetime import datetime, timedelta

# Record the start and current time
start_time = datetime.now()
now_time = datetime.now()

# Run a loop for three hours
while (now_time < start_time + timedelta(minutes=180)):
    if light == 'Light':
        # funzione capture
        row = (datetime.now(), location.latitude.signed_dma, location.longitude.signed_dms, location.elevation.km, sense.temperature, sense.humidity)
        'row = (datetime.now(), location.latitude.degrees, location.longitude.degrees, location.elevation.km, sense.temperature, sense.humidity)'
        add_csv_data(data_file, row)
        sleep(30)
        # Update the current time
        now_time = datetime.now()
