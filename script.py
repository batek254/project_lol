#loading riotwatche
from riotwatcher import LolWatcher, ApiError
import pandas as pd
import matplotlib.pyplot as plt

#linking with api
#remember not to revoke api key
lol_watcher = LolWatcher('<api-key>')

#selecting region
my_region = 'euw1'

#tests
#selecting no.1 summoner on west (05.11.2020) by name to obtain secret account ID
summoner = lol_watcher.summoner.by_name(my_region, 'HAHHAHAHAHAHXDDD')

#getting match list of summoner to obtain match ID
match_list = lol_watcher.match.matchlist_by_account(my_region, summoner['accountId'])

#print game ID of first match in history
print(match_list['matches'][1]['gameId'])

#getting match data
match = lol_watcher.match.by_id(my_region, match_list['matches'][1]['gameId'])

#printing match data
print(match)

#Cycuszki

#commit test

# champions analyze
latest = lol_watcher.data_dragon.versions_for_region(my_region)['n']['champion']
static_champ_list = lol_watcher.data_dragon.champions(latest, False, 'en_US')

# champ static list data to dict for looking up
champ_df = pd.DataFrame(columns=['id','name','attack','defense','magic','difficulty','role','hp','movespeed','armor',
                                 'attackrange','damage','attackspeed'])
champ_dict = {}
i = 0
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_df = champ_df.append({'id': row['key'], 'name': key, 'attack': row['info']['attack'],
                               'defense': row['info']['defense'], 'magic': row['info']['magic'],
                                'difficulty': row['info']['difficulty'], 'role': row['tags'],
                                'hp': row['stats']['hp'], 'movespeed': row['stats']['movespeed'],
                                'armor': row['stats']['armor'], 'attackrange': row['stats']['attackrange'],
                                'damage': row['stats']['attackdamage'], 'attackspeed': row['stats']['attackspeed']}, ignore_index=True)
print(champ_df)
champ_df.iloc[1:round(len(champ_df)/2),:].plot(x='name',kind='bar', stacked=True, colormap='Paired')
champ_df.iloc[round(len(champ_df)/2):len(champ_df),:].plot(x='name',kind='bar', stacked=True, colormap='Paired')

champ_df.iloc[1:round(len(champ_df)/2),:].plot.bar(x='name', y=['armor','defense', 'hp'])
champ_df.iloc[round(len(champ_df)/2):len(champ_df),:].plot.bar(x='name', y=['armor','defense', 'hp'])

champ_df.iloc[1:round(len(champ_df)/2),:].plot.bar(x='name', y=['attack','damage', 'attackspeed', 'attackrange'])
champ_df.iloc[round(len(champ_df)/2):len(champ_df),:].plot.bar(x='name', y=['attack','damage', 'attackspeed', 'attackrange'])