from models import Game, Inning, AtBat, Pitch, Player
import os
import sys
import datetime
import requests
import time
from lxml import etree
from natural import number
from papirus import PapirusTextPos


now = datetime.datetime.now() 
fontPath = os.path.dirname(os.path.abspath(__file__)) + '/fonts/benton-sans-regular.ttf'
dingsPath =os.path.dirname(os.path.abspath(__file__)) + '/fonts/FreeSans.ttf'
display = PapirusTextPos(False)
minX = 0
minY = 0

# ---------------------------------------------------------------------

def writeToDisplay(text = '', x = 2, y = 2, size = 14, id = 'Default', fontPath = fontPath):
    display.AddText(text=text, x=x, y=y, size=size, Id=id, invert=False, font_path=fontPath)
    print(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S %Z') + ': ' + text)
    print('')
    return

# ---------------------------------------------------------------------

def getCount(howMany, max):
    count = ''
    if int(howMany) == 4 and max == 4:
        count = u"\u25CF \u25CF \u25CF \u25CF"
    elif int(howMany) == 3 and max == 4:
        count = u"\u25CF \u25CF \u25CF \u25CB"
    elif int(howMany) == 2 and max == 4:
        count = u"\u25CF \u25CF \u25CB \u25CB"
    elif int(howMany) == 1 and max == 4:
        count = u"\u25CF \u25CB \u25CB \u25CB"
    elif int(howMany) == 0 and max == 4:
        count = u"\u25CB \u25CB \u25CB \u25CB"
    elif int(howMany) == 3:
        count = u"\u25CF \u25CF \u25CF"
    elif int(howMany) == 2:
        count = u"\u25CF \u25CF \u25CB"
    elif int(howMany) == '1':
        count = u"\u25CF \u25CB \u25CB"
    else:
        count = u"\u25CB \u25CB \u25CB"
    return count

# ---------------------------------------------------------------------

def getPitchType(pitch):
    pitchTypeAbbreviation = pitch.pitchType
    return {
        'CB' : 'Curveball',
        'CH' : 'Changeup',
        'CU' : 'Curveball',
        'EP' : 'Eephus',
        'FA' : 'Fastball',
        'FC' : 'Fastball (Cutter)',
        'FF' : 'Four-Seam Fastball',
        'FO' : 'Pitch Out',
        'FS' : 'Fastball',
        'FT' : 'Two-Seam Fastball',
        'KC' : 'Knuckle-curve',
        'KN' : 'Knuckleball',
        'PO' : 'Pitch Out',
        'SF' : 'Fastball (Split-Fingered)',
        'SI' : 'Fastball (Sinker)',
        'SL' : 'Slider'
    }[pitchTypeAbbreviation] or ''

# ---------------------------------------------------------------------

def getTeamAbbreviation(team):
    return {
        'Angels' : 'LAA',
        'Astros' : 'HOU',
        'Athletics' : 'OAK',
        'Blue Jays' : 'TOR',
        'Braves' : 'ATL',
        'Brewers' : 'MIL',
        'Cardinals' : 'SLN',
        'Cubs' : 'CHN',
        'D-backs' : 'ARI',
        'Dodgers' : 'LAD',
        'Giants' : 'SF',
        'Indians' : 'CLE',
        'Mariners' : 'SEA',
        'Marlins' : 'MIA',
        'Mets' : 'NYM',
        'Nationals' : 'WAS',
        'Orioles' : 'BAL',
        'Padres' : 'SD',
        'Phillies' : 'PHL',
        'Pirates' : 'PIT',
        'Rangers' : 'TEX',
        'Rays' : 'TB',
        'Red Sox' : 'BOS',
        'Reds' : 'CIN',
        'Rockies' : 'COL',
        'Royals' : 'KAN',
        'Tigers' : 'DET',
        'Twins' : 'MIN',
        'White Sox' : 'CWS',
        'Yankees' : 'NYY'
    }[team] or team

# ---------------------------------------------------------------------

def getAtBatTeam(game, atBat):
    if getTeamAbbreviation(game.team) == atBat.batter.team:
        output = '[' + game.team + '] vs. ' + game.opponent
    elif getTeamAbbreviation(game.opponent) == atBat.batter.team:
        output = game.team + ' vs.  [' + game.opponent + ']'
    else:
        output = game.team + ' vs. ' + game.opponent
    return output

# ---------------------------------------------------------------------

def displayBoxScore(game, inning):
    display.Clear()
    if game.status == 'FINAL': 
        writeToDisplay('FINAL', minX, minY, 14, 'BoxScoreInning', fontPath)
    else: 
        writeToDisplay(inning.half + ' ' + number.ordinal(inning.number), minX, minY, 14, 'BoxScoreInning', fontPath)

    writeToDisplay('R', 125, 30, 14, 'RunsHeader', fontPath)
    writeToDisplay('H', 150, 30, 14, 'HitsHeader', fontPath)
    writeToDisplay('E', 175, 30, 14, 'ErrorsHeader', fontPath)
    
    writeToDisplay(game.team, minX, 50, 14, 'Team', fontPath)
    writeToDisplay(game.teamRuns, 125, 50, 14, 'TeamRuns', fontPath)
    writeToDisplay(game.teamHits, 150, 50, 14, 'TeamHits', fontPath)
    writeToDisplay(game.teamErrors, 175, 50, 14, 'TeamErrors', fontPath)
    
    writeToDisplay(game.opponent, minX, 70, 14, 'Opponent', fontPath)
    writeToDisplay(game.opponentRuns, 125, 70, 14, 'OpponentRuns', fontPath)
    writeToDisplay(game.opponentHits, 150, 70, 14, 'OpponentHits', fontPath)
    writeToDisplay(game.opponentErrors, 175, 70, 14, 'OpponentErrors', fontPath)
    
    display.WriteAll(partial_update=True)
    return

# ---------------------------------------------------------------------

def displayPitch(game, atBat, pitch):
    display.Clear()
    writeToDisplay(getAtBatTeam(game, atBat), minX, minY, 14, 'Versus', fontPath)
    
    writeToDisplay('Pitching: ' + atBat.pitcher.first + ' ' + atBat.pitcher.last, minX, 30, 12, 'Pitcher', fontPath)
    writeToDisplay(str(atBat.pitcher.era) + ' ERA', 160, 30, 10, 'PitcherStats', fontPath)
    writeToDisplay(str(pitch.speed) + ' MPH ' + getPitchType(pitch), minX, 45, 10, 'Pitch', fontPath)
    writeToDisplay('At Bat: ' + atBat.batter.first + ' ' + atBat.batter.last + ' (#' + str(atBat.batter.number) + ' ' + atBat.batter.position + ')', minX, 60, 12, 'Batter', fontPath)
    writeToDisplay(str(atBat.batter.avg) + ' AVG, ' + str(atBat.batter.hr) + ' HR', 160, 60, 10, 'BatterStats', fontPath)
    writeToDisplay(pitch.callDescription, minX, 75, 10, 'Call', fontPath)
    display.WriteAll(partial_update=True)
    return

# ---------------------------------------------------------------------

def displayPlay(game, atBat, pitch):
    baseDefault = u"\u25C7"
    baseHighlight = u"\u25C6"
    
    display.Clear()
    writeToDisplay(getAtBatTeam(game, atBat), minX, minY, 14, 'Versus', fontPath)
    writeToDisplay(atBat.description, minX, 20, 10, 'Description')

    writeToDisplay('B', minX, 45, 12, 'BallsLabel', fontPath)
    writeToDisplay(getCount(atBat.balls, 4), 25, 45, 12, 'BallsCount', dingsPath)
    writeToDisplay('S', minX, 60, 12, 'StrikesLabel', fontPath)
    writeToDisplay(getCount(atBat.strikes, 3), 25, 60, 12, 'StrikesCount', dingsPath)
    writeToDisplay('O', minX, 75, 12, 'OutsLabel', fontPath)
    writeToDisplay(getCount(atBat.outs, 3), 25, 75, 12, 'OutsCount', dingsPath)
    
    if atBat.onFirst is not None:
        writeToDisplay(baseHighlight, 170, 60, 20, 'FirstBase', dingsPath)
    else:
        writeToDisplay(baseDefault, 170, 60, 20, 'FirstBase', dingsPath)
    
    if atBat.onSecond is not None:
        writeToDisplay(baseHighlight, 150, 45, 20, 'SecondBase', dingsPath)
    else:
        writeToDisplay(baseDefault, 150, 45, 20, 'SecondBase', dingsPath)
    
    if atBat.onThird is not None:
        writeToDisplay(baseHighlight, 130, 60, 20, 'ThirdBase', dingsPath)
    else:
        writeToDisplay(baseDefault, 130, 60, 20, 'ThirdBase', dingsPath)
    display.WriteAll(partial_update=True)
    return
    
# ---------------------------------------------------------------------

def displayInGame(game, inning, atBat, pitch, interval):
    if game.status == 'FINAL':
        displayBoxScore(game, inning)
        time.sleep(interval)
    else:
        displayBoxScore(game, inning)
        time.sleep(interval/3)
        displayPitch(game, atBat, pitch)
        time.sleep(interval/3)
        displayPlay(game, atBat, pitch)
        time.sleep(interval/3)
    return 

# ---------------------------------------------------------------------

def displayStatus(message, wait):
    display.Clear()
    writeToDisplay(message, minX, minY, 14, 'Status', fontPath)
    display.WriteAll(partial_update=True)
    time.sleep(wait)
    return 

 # --------------------------------------------------------------------

def getPlayer(players, playerID):
    playerRoot = players.xpath("/game/team/player[@id='" + playerID + "']")[0]
    player = Player()
    player.id = playerID
    player.first = playerRoot.get('first')
    player.last = playerRoot.get('last')
    player.team = playerRoot.get('team_abbrev')
    player.number = playerRoot.get('num')
    player.handed = playerRoot.get('rl')
    player.bats = playerRoot.get('bats')
    player.position = playerRoot.get('position')
    player.status = playerRoot.get('status')
    player.avg = '{0:.3f}'.format(float(playerRoot.get('avg')))
    player.hr = playerRoot.get('hr')
    player.rbi = playerRoot.get('rbi')
    if player.position == 'P':
        player.wins = playerRoot.get('wins')
        player.losses = playerRoot.get('losses')
        player.era = '{0:.2f}'.format(float(playerRoot.get('era')))
    return player

# ---------------------------------------------------------------------

def getLatestEvent(game, eventsUrl, players, scoreboardUrl, interval = 60):
    try:
        inning = Inning()
        atBat = AtBat()
        pitch = Pitch()

        scoreboardRequest = requests.get(scoreboardUrl)
        scoreboardDocumentBytes = bytes(bytearray(scoreboardRequest.text, encoding='utf-8'))
        scoreboardDocumentXML = etree.XML(scoreboardDocumentBytes)
        gameRoot = scoreboardDocumentXML.xpath("/scoreboard/*/game[@id='" + game.id + "']")[0]
        
        gameStatus = gameRoot.get('status')
        if gameStatus == 'FINAL' or gameStatus == 'GAME_OVER':
            game.status = 'FINAL'
        
        outs = gameRoot.getparent().get("outs") or 0  # MLB stores items in multiple places?
        parentIter = gameRoot.getparent().iter()
        for child in parentIter:
            if child.tag == 'team' and child.get('name') == game.team:
                game.teamRuns = child.getchildren()[0].get('R')
                game.teamHits = child.getchildren()[0].get('H')
                game.teamErrors = child.getchildren()[0].get('E')
            if child.tag == 'team' and child.get('name') != game.team:
                game.opponent = child.get('name')
                game.opponentRuns = child.getchildren()[0].get('R')
                game.opponentHits = child.getchildren()[0].get('H')
                game.opponentErrors = child.getchildren()[0].get('E')

        gameEventsRequest = requests.get(eventsUrl)
        # print(gameEventsRequest.text)
        gameEventsDocumentBytes = bytes(bytearray(gameEventsRequest.text, encoding='utf-8'))
        gameEventsDocumentXML = etree.XML(gameEventsDocumentBytes)
        
        # Get current/most recent inning
        inningRoot = gameEventsDocumentXML.xpath('/game/inning[last()]')[0]
        inning.number = inningRoot.get('num') or 0
        inning.half = (inningRoot.xpath("/game/inning[last()]/*[text() and string-length()>0][last()]")[0]).tag or ''
        atBatRoot = gameEventsDocumentXML.xpath("/game/inning[last()]/*[text() and string-length()>0][last()]/atbat[last()]")[0]
        atBatPlayerRoot = gameEventsDocumentXML.xpath("/game/atBat")[0]
        atBat.number = atBatRoot.get('num') or 0
        atBat.balls = atBatRoot.get('b') or 0
        atBat.strikes = atBatRoot.get('s') or 0
        atBat.outs = atBatRoot.get('o') or outs
        try: 
            atBat.pitcher = getPlayer(players, atBatPlayerRoot.get('pid'))
        except:
            atBat.pitcher = getPlayer(players, atBatRoot.get('pitcher'))
        atBat.batter = getPlayer(players, atBatRoot.get('batter'))
        if len(atBatRoot.get('b1')) > 0:
            atBat.onFirst = getPlayer(players, atBatRoot.get('b1'))
        if len(atBatRoot.get('b2')) > 0:
            atBat.onSecond = getPlayer(players, atBatRoot.get('b2'))
        if len(atBatRoot.get('b3')) > 0:
            atBat.onThird = getPlayer(players, atBatRoot.get('b3'))
        atBat.description = atBatRoot.get('des') or ''
        atBat.guid = atBatRoot.get('play_guid') or ''
        trackAtBatID = atBat.number

        # Get current/most recent pitch of the inning
        pitchRoot = gameEventsDocumentXML.xpath("/game/inning[last()]/*[text() and string-length()>0][last()]/atbat[last()]/pitch[last()]")[0]
        pitch.id = pitchRoot.get('sv_id') or ''
        pitch.call = pitchRoot.get('type') or ''
        pitch.callDescription = pitchRoot.get('des') or ''
        pitch.speed = pitchRoot.get('start_speed') or 0
        pitch.pitchType = pitchRoot.get('pitch_type') or ''
        trackPitchID = pitch.id
        
        displayInGame(game, inning, atBat, pitch, interval)
    except:
        pass

    if game.status != 'FINAL':
        return True
    else:
        time.sleep(3600)
        return False
    
# ---------------------------------------------------------------------
