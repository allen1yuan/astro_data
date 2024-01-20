from opencage.geocoder import OpenCageGeocode
import pandas as pd
import csv
key = "777b0b23e521498eacfdb902c79539f3"
geocoder = OpenCageGeocode(key)
df = pd.read_csv('datathon_2024_dataset.csv')
index = df.columns.get_loc('Away City')
lats = []
lngs = []
final_lats = []
final_lngs = []
final_home_lats = []
final_home_lngs = []
cities = ['Phoenix AZ', 'Atlanta GA', 'Baltimore MD', 'Boston MA', 'Chicago IL', 'Cincinnati OH', 'Cleveland OH', 'Denver CO', 'Detroit MI', 'Houston TX', 'Kansas City MO', 'Anaheim CA', 'Los Angeles CA', 'Milwaukee WI', 'Minneapolis MN',
          'New York NY', 'Miami FL', 'Montreal QUE', 'Oakland CA', 'Philadelphia PA', 'Pittsburgh PA', 'San Diego CA', 'San Francisco CA', 'Seattle WA', 'St. Louis MO', 'Arlington TX', 'Toronto ONT', 'Washington DC', 'Tokyo JAP',
          'St. Petersburg FL', 'San Juan PR', 'Lake Buena Vista FL', 'Sydney AU', 'Fort Bragg NC']
for city in cities:
    results = geocoder.geocode(city)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    lats.append(lat)
    lngs.append(lng)
    print(city, lat, lng)

for city in df['Away City']:
    for cityName in cities:
        if cityName == city:
            index = cities.index(cityName)
            lat = lats[index]
            lng = lngs[index]
            final_lats.append(lat)
            final_lngs.append(lng)
df.insert(5, 'Away City Latitude', final_lats)
df.insert(6, 'Away City Longitude', final_lngs)

df.to_csv('datathon_2024_dataset.csv', index=False)

df = pd.DataFrame()
df = pd.read_csv('datathon_2024_dataset.csv')
homeIndex = df.columns.get_loc('city')
foundCity = False

for city in df['city']:
    for cityName in cities:
        if not foundCity:
            if cityName == city:
                index = cities.index(cityName)
                lat = lats[index]
                lng = lngs[index]
                final_home_lats.append(lat)
                final_home_lngs.append(lng)
                foundCity = True
    if foundCity == False:
        geocoder.geocode(city)
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print("Special", city, lat, lng)
        final_home_lats.append(lat)
        final_home_lngs.append(lng)
    foundCity = False


df.insert(11, 'Home City Latitude', final_home_lats)
df.insert(12, 'Home City Longitude', final_home_lngs)
df.to_csv('datathon_2024_dataset.csv', index=False)
