#loading riotwatche
from riotwatcher import LolWatcher, ApiError

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
