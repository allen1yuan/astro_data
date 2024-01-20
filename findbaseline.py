import csv
import pandas as pd

df = pd.read_csv('datathon_clean.csv')

citymap = {'ARI': 'Phoenix AZ',
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
           'MIA': 'St. Petersburg FL', }

homeperformancekey = {
    'ARI': 0,
    'ATL': 0,
    'BAL': 0,
    'BOS': 0,
    'CHN': 0,
    'CHA': 0,
    'CIN': 0,
    'CLE': 0,
    'COL': 0,
    'DET': 0,
    'HOU': 0,
    'KCA': 0,
    'ANA': 0,
    'LAN': 0,
    'MIL': 0,
    'MIN': 0,
    'NYN': 0,
    'FLO': 0,
    'MON': 0,
    'NYA': 0,
    'OAK': 0,
    'PHI': 0,
    'PIT': 0,
    'SDN': 0,
    'SFN': 0,
    'SEA': 0,
    'SLN': 0,
    'TBA': 0,
    'TEX': 0,
    'TOR': 0,
    'WAS': 0,
    'MIA': 0,
}

for team in citymap.keys():
    for index, row in df.iterrows():
        datateam = row['home_team']
        # replace 'home_team_homeruns' with the actual column name
        homeruns = row['home_hr']
        homescore = row['home_score']
        home_pa = row['home_pa']
        home_1b = row['home_1b']
        home_2b = row['home_2b']
        home_3b = row['home_3b']
        home_fo = row['home_fo']
        home_so = row['home_so']

        home_bb = row['home_bb']
        home_hbp = row['home_hbp']

        if team == datateam:
            homeperformancekey[team] += (homeruns + homescore + home_pa + home_1b +
                                         home_2b + home_3b + home_fo + home_so - home_bb - home_hbp)

print(homeperformancekey)
