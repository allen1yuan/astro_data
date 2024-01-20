import pandas as pd
import csv

df = pd.read_csv('datathon_2024_dataset.csv')

df['city'] = df['city'] + ' ' + df['state']
df.to_csv('datathon_2024_dataset.csv', index=False)
