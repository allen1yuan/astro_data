import csv
import pandas as pd
from opencage.geocoder import OpenCageGeocode
from geopy.distance import geodesic
df = pd.read_csv('data.csv')


def findDistance(lat_A, lng_A, lat_B, lng_B):
    key = "777b0b23e521498eacfdb902c79539f3"
    geocoder = OpenCageGeocode(key)
    return (geodesic((lat_A, lng_A), (lat_B, lng_B)).kilometers)


lats = df['Away City Latitude']
lngs = df['Away City Longitude']
home_lats = df['Home City Latitude']
home_lngs = df['Home City Longitude']
distances = []
for i in range(len(df['Away City Latitude'])):
    distance = findDistance(lats[i], lngs[i], home_lats[i], home_lngs[i])
    distances.append(round(distance, 3))

df.insert(15, 'DistanceKM', distances)


df.to_csv('data.csv', index=False)
