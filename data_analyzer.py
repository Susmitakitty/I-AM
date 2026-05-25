import csv

filename = "asset_data.csv"

total_temp = 0
total_vibration = 0
count = 0

with open(filename, 'r') as csvfile:

    reader = csv.DictReader(csvfile)

    for row in reader:

        total_temp += float(row['temperature'])
        total_vibration += float(row['vibration'])

        count += 1

avg_temp = total_temp / count
avg_vibration = total_vibration / count

with open("analysis_summary.txt", "w") as f:

    f.write(f"Average Temperature = {avg_temp:.2f} C\n")

    f.write(f"Average Vibration = {avg_vibration:.2f}\n")

print("Analysis completed")