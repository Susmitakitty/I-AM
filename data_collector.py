import csv
import time
import random
from datetime import datetime

filename = "asset_data.csv"

def collect_data():

    fieldnames = ['timestamp', 'asset_id', 'temperature', 'vibration']

    with open(filename, 'a', newline='') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        for i in range(5):

            data = {
                'timestamp': datetime.now(),
                'asset_id': 'Asset-1',
                'temperature': random.randint(20,80),
                'vibration': random.randint(1,5)
            }

            writer.writerow(data)

            print(data)

            time.sleep(2)

if __name__ == "__main__":
    collect_data()