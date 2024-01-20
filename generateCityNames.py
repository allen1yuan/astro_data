from opencage.geocoder import OpenCageGeocode
import pandas as pd
import csv
key = "777b0b23e521498eacfdb902c79539f3"
geocoder = OpenCageGeocode(key)
team_dict = {
    'ARI': 'Arizona Diamondbacks',
    'ATL': 'Atlanta Braves',
    'BAL': 'Baltimore Orioles',
    'BOS': 'Boston Red Sox',
    'CHN': 'Chicago Cubs',
    'CHA': 'Chicago White Sox',
    'CIN': 'Cincinnati Reds',
    'CLE': 'Cleveland Indians',
    'COL': 'Colorado Rockies',
    'DET': 'Detroit Tigers',
    'HOU': 'Houston Astros',
    'KCA': 'Kansas City Royals',
    'ANA': 'Los Angeles Angels',
    'LAN': 'Los Angeles Dodgers',
    'MIL': 'Milwaukee Brewers',
    'MIN': 'Minnesota Twins',
    'NYN': 'New York Mets',
    'FLO': 'Miami Marlins',
    'MON': 'Montreal Expos',
    'NYA': 'New York Yankees',
    'OAK': 'Oakland Athletics',
    'PHI': 'Philadelphia Phillies',
    'PIT': 'Pittsburgh Pirates',
    'SDN': 'San Diego Padres',
    'SFN': 'San Francisco Giants',
    'SEA': 'Seattle Mariners',
    'SLN': 'St. Louis Cardinals',
    'TBA': 'Tampa Bay Rays',
    'TEX': 'Texas Rangers',
    'TOR': 'Toronto Blue Jays',
    'WAS': 'Washington Nationals'
}
city_dict = {
    'Arizona Diamondbacks': 'Phoenix AZ',
    'Atlanta Braves': 'Atlanta GA',
    'Baltimore Orioles': 'Baltimore MD',
    'Boston Red Sox': 'Boston MA',
    'Chicago Cubs': 'Chicago IL',
    'Chicago White Sox': 'Chicago IL',
    'Cincinnati Reds': 'Cincinnati OH',
    'Cleveland Indians': 'Cleveland OH',
    'Colorado Rockies': 'Denver CO',
    'Detroit Tigers': 'Detroit MI',
    'Houston Astros': 'Houston TX',
    'Kansas City Royals': 'Kansas City MO',
    'Los Angeles Angels': 'Anaheim CA',
    'Los Angeles Dodgers': 'Los Angeles CA',
    'Milwaukee Brewers': 'Milwaukee WI',
    'Minnesota Twins': 'Minneapolis MN',
    'New York Mets': 'New York NY',
    'Miami Marlins': 'Miami FL',
    'Montreal Expos': 'Montreal QC',
    'New York Yankees': 'New York NY',
    'Oakland Athletics': 'Oakland CA',
    'Philadelphia Phillies': 'Philadelphia PA',
    'Pittsburgh Pirates': 'Pittsburgh PA',
    'San Diego Padres': 'San Diego CA',
    'San Francisco Giants': 'San Francisco CA',
    'Seattle Mariners': 'Seattle WA',
    'St. Louis Cardinals': 'St. Louis MO',
    'Tampa Bay Rays': 'Tampa Bay FL',
    'Texas Rangers': 'Arlington TX',
    'Toronto Blue Jays': 'Toronto ON',
    'Washington Nationals': 'Washington DC'
}


df = pd.read_csv('city_distance.csv')
df['Team Name'] = df['away_team'].map(team_dict)
df.to_csv('city_distance.csv', index=False)
df['City'] = df['Team Name'].map(city_dict)
df.to_csv('city_distance.csv', index=False)
