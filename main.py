import os
import pandas as pd


os.makedirs('convertedfiles', exist_ok=True)

count = 0
for excelFile in os.listdir('.'):

    if not excelFile.endswith(('.xlsx', '.xls')):
        continue

    count += 1
    df = pd.read_excel(excelFile)
    newFileName = os.path.basename(excelFile)
    df.to_csv(newFileName.replace('.xlsx', '.csv'), index=None, header=True)
print(f"{count} Excel files found")
print('Converted Excel Files To CSV Files')
