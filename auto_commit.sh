#!/bin/bash 
git pull origin main 
# Run analyzer & generate report as a simple test 
python3 data_analyzer.py 
python3 generate_report.py 
 
if [ $? -eq 0 ]; then 
  git add . 
  echo "Enter commit message:" 
  read msg 
  git commit -m "$msg" 
  git push origin $(git branch --show-current) 
else 
  echo "Tests failed. Commit aborted." 
fi 