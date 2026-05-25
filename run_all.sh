#!/bin/bash 
# Run all project scripts in order 
echo "Starting Data Collection for 30 seconds..." 
timeout 30 python data_collector.py 
 
echo "Analyzing data..." 
python data_analyzer.py 
 
echo "Generating PDF report..." 
python generate_report.py