from models import Game, Inning, AtBat, Pitch, Player
from functions import getLatestEvent, displayStatus
import os
import sys
import argparse
import datetime
import requests
import time
from lxml import etree

parser = argparse.ArgumentParser()
parser.add_argument('--team', dest="team", help='MLB team name')
parser.add_argument('--refresh', dest='refresh', help='Refresh rate (in seconds)')
args = parser.parse_args()

teamName = args.team or 'D-backs'
updateInterval = args.refresh or 15

now = datetime.datetime.now() 
#now = datetime.date(2019, 2, 23) # for development purposes only

displayStatus('', 0) # Clear the screen

scoreboardUrl = 'http://gd2.mlb.com/components/game/mlb/year_' + now.strftime('%Y') + '/month_' + now.strftime('%m') + '/day_' + now.strftime('%d') + '/scoreboard.xml'
scoreboardRequest = requests.get(scoreboardUrl)
#print(scoreboardRequest.text)
scoreboardDocumentBytes = bytes(bytearray(scoreboardRequest.text, encoding='utf-8'))
scoreboardDocumentXML = etree.XML(scoreboardDocumentBytes)

gameCount = scoreboardDocumentXML.xpath("count(/scoreboard/*/team[@name='" + teamName + "'])")
#print(gameCount)
if gameCount > 0:
    gameInitRoot = scoreboardDocumentXML.xpath("/scoreboard/*/team[@name='" + teamName + "']")[0].getparent()
    #print(etree.tostring(gameInitRoot))
    game = Game()

    if gameCount > 1:
        # TODO: Test logic in case of doubleheader
        gameRootFiltered = gameInitRoot.findall(".//game[@status!='FINAL' and @status!='GAME_OVER']")[0]
    else:
        gameRootFiltered = gameInitRoot.findall(".//game")[0]
   
    game.id = gameRootFiltered.get('id')
    game.team = teamName
    game.status = gameRootFiltered.get('status')
    trackAtBatID = 0
    trackPitchID = 0

    gamePlayersUrl = 'http://gd2.mlb.com/components/game/mlb/year_' + now.strftime('%Y') + '/month_' + now.strftime('%m') + '/day_' + now.strftime('%d') + '/gid_' + game.id + '/players.xml'
    #print(gamePlayersUrl)
    while requests.get(gamePlayersUrl).status_code != 200:
        displayStatus('Awaiting player roster', 300)

    gamePlayersRequest = requests.get(gamePlayersUrl)
    #print(gamePlayersRequest.text)
    gamePlayersDocumentBytes = bytes(bytearray(gamePlayersRequest.text, encoding='utf-8'))
    gamePlayersDocumentXML = etree.XML(gamePlayersDocumentBytes)
    
    gameEventsUrl = 'http://gd2.mlb.com/components/game/mlb/year_' + now.strftime('%Y') + '/month_' + now.strftime('%m') + '/day_' + now.strftime('%d') + '/gid_' + game.id + '/game_events.xml'
    #print(gameEventsUrl)
    while requests.get(gameEventsUrl).status_code != 200:
        displayStatus('Awaiting game data...', 300)
    
    isRunning = True
    while isRunning == True:
        isRunning = getLatestEvent(game, gameEventsUrl, gamePlayersDocumentXML, scoreboardUrl, updateInterval)
    if isRunning == False:
        os.execv(__file__, sys.argv)
else:
    displayStatus('There is no game scheduled for the ' + teamName + ' today.', 60)