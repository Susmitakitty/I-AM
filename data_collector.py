import csv 
import time 
import random 
from datetime import datetime 
filename = "asset_data.csv" 
def collect_data(): 
fieldnames = ['timestamp', 'asset_id', 'temperature', 'vibration'] 
try: 
with open(filename, 'a', newline='') as csvfile: 
     writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
            # Write header if file empty 
            if csvfile.tell() == 0: 
                writer.writeheader() 
            while True: 
                data = { 
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
                    'asset_id': f"Asset-{random.randint(1,5)}", 
                    'temperature': round(random.uniform(20.0, 80.0), 2), 
                    'vibration': round(random.uniform(0.1, 5.0), 2) 
                } 
                writer.writerow(data) 
                print(f"Logged: {data}") 
                time.sleep(10)  # Simulate delay 
    except KeyboardInterrupt: 
        print("Data collection stopped by user.") 
 
if __name__ == "__main__": 
    collect_data()