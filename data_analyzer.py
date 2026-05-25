import csv 
from collections import defaultdict 
 
filename = "asset_data.csv" 
summary_file = "analysis_summary.txt" 
 
def analyze_data(): 
    temp_sums = defaultdict(float) 
    vib_sums = defaultdict(float) 
    counts = defaultdict(int) 
 
    with open(filename, 'r') as csvfile: 
        reader = csv.DictReader(csvfile) 
        for row in reader: 
            asset = row['asset_id'] 
            temp_sums[asset] += float(row['temperature']) 
            vib_sums[asset] += float(row['vibration']) 
            counts[asset] += 1 
 
    with open(summary_file, 'w') as f: 
        f.write("Asset Analysis Summary:\n\n") 
        for asset in counts: 
            avg_temp = temp_sums[asset] / counts[asset] 
            avg_vib = vib_sums[asset] / counts[asset] 
            f.write(f"{asset}: Avg Temp = {avg_temp:.2f} C, Avg Vibration = 
{avg_vib:.2f} m/s²\n") 
    print(f"Analysis written to {summary_file}") 
 
if __name__ == "__main__": 
    analyze_data() s
