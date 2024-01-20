import pandas as pd
import csv

df = pd.read_csv('datathon_2024_dataset.csv')


def use_bus(distance):
    return distance <= 350


use_bus_series = df['DistanceKM'].apply(use_bus)

# Insert the 'useBus' column at position 16
df.insert(16, 'useBus', use_bus_series)

df.to_csv('datathon_2024_dataset.csv', index=False)
