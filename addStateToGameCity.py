import pandas as pd
import csv

df = pd.read_csv('data.csv')

df['city'] = df['city'] + ' ' + df['state']
df.to_csv('data.csv', index=False)
