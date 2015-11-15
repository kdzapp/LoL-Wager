from riotwatcher import RiotWatcher
import time

leagueApi = RiotWatcher('04328930-7ab0-4e23-8c83-af1bbc4147ea')

#Get Summoner ID and Stats
summoner = raw_input("Enter your summoner name: ")
opponent = raw_input("Enter your opponent's summoner name:")

if leagueApi.can_make_request():
    summonerId = leagueApi.get_summoner(name=summoner)
    opponentId = leagueApi.get_summoner(name=opponent)
    print
    print "Welcome Summoner!"
    bet = raw_input("Enter the amount of $ you would like to bet: ")
    print
    print "You've bet", bet, "dollars"

    lastPlayedGame = leagueApi.get_recent_games(summonerId['id'])['games'][0]['createDate']
    currentDate = lastPlayedGame

    print "Waiting for you to play a game!"
    while lastPlayedGame == currentDate:
        #Checks every 10 seconds for new game
        time.sleep(10)
        currentDate = leagueApi.get_recent_games(summonerId['id'])['games'][0]['createDate']

    #Need to also make a check to see if the other player was playing
    summonerGameId = leagueApi.get_recent_games(summonerId['id'])['games'][0]['gameId']
    opponentGameId = leagueApi.get_recent_games(opponentId['id'])['games'][0]['gameId']
    
    if summonerGameId == opponentGameId:
        if leagueApi.get_recent_games(summonerId['id'])['games'][0]['stats']['win']:
            print "You have beat your enemy! You win", bet, "dollars!"
        else:
            print "You have lost to your enemy! You lose", bet, "dollars!"
    else:
        "Your last game was not played with the intended opponent!"
        
else:
    "I'm Sorry, we can't connect to the server right now!"

#Ignore this example
#recentGame = test.get_recent_games(me['id'])
#print recentGame

#Use Summoner ID to get Stats
#statSummary = test.get_stat_summary(me['id'])
#playerStats = statSummary['playerStatSummaries']
#unrankedStats = playerStats[7]
#wins = unrankedStats['wins']
