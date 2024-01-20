import pandas as pd
import csv
CityAbbrvDict = {
    'ARI': 'Phoenix AZ',
    'ATL': 'Atlanta GA',
    'BAL': 'Baltimore MD',
    'BOS': 'Boston MA',
    'CHN': 'Chicago IL',
    'CHA': 'Chicago IL',
    'CIN': 'Cincinnati OH',
    'CLE': 'Cleveland OH',
    'COL': 'Denver CO',
    'DET': 'Detroit MI',
    'HOU': 'Houston TX',
    'KCA': 'Kansas City MO',
    'ANA': 'Anaheim CA',
    'LAN': 'Los Angeles CA',
    'MIL': 'Milwaukee WI',
    'MIN': 'Minneapolis MN',
    'NYN': 'New York NY',
    'FLO': 'Miami FL',
    'MON': 'Montreal QUE',
    'NYA': 'New York NY',
    'OAK': 'Oakland CA',
    'PHI': 'Philadelphia PA',
    'PIT': 'Pittsburgh PA',
    'SDN': 'San Diego CA',
    'SFN': 'San Francisco CA',
    'SEA': 'Seattle WA',
    'SLN': 'St. Louis MO',
    'TBA': 'St. Petersburg FL',
    'TEX': 'Arlington TX',
    'TOR': 'Toronto ONT',
    'WAS': 'Washington DC',
    'MIA': 'St. Petersburg FL',

}
df = pd.read_csv('datathon_2024_dataset.csv')
new_column = df['away_team'].map(CityAbbrvDict)
df.insert(4, 'Away City', new_column)
df.to_csv('datathon_2024_dataset.csv', index=False)
