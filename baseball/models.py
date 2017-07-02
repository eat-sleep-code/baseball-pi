# ---------------------------------------------------------------------

class Game(object):
    id = ''
    status = ''
    team = ''
    teamRuns = 0
    teamHits = 0
    teamErrors = 0
    opponent = ''
    opponentRuns = 0
    opponentHits = 0
    opponentErrors = 0

    def make_game(id, status, team, teamRuns, teamHits, teamErrors, opponent, opponentRuns, opponentHits, opponentErrors):
        game = Game()
        game.id = id
        game.status = status
        game.team = team
        game.teamRuns = teamRuns
        game.teamHits = teamHits    
        game.teamErrors = teamErrors
        game.opponent = opponent
        game.opponentRuns = opponentRuns
        game.opponentHits = opponentHits
        game.opponentErrors = opponentErrors

# ---------------------------------------------------------------------

class Inning(object):
    number = 0
    half = 'top'

    def make_inning(number, half):
        inning = Inning()
        inning.number = number
        inning.half = half

# ---------------------------------------------------------------------

class Player(object):
    id = ''
    first = ''
    last = ''
    team = ''
    number = 0
    handed = ''
    bats = ''
    position = ''
    status = ''
    avg = '.000'
    hr = 0
    rbi = 0
    wins = 0
    losses = 0
    era = 0

    def make_player (id, first, last, team, number, handed, bats, position, status, avg, hr, rbi, wins, losses, era):
        player = Player()
        player.id = id
        player.first = first
        player.last = last
        player.team = team
        player.number = number
        player.handed = rl
        player.bats = bats
        player.position = position
        player.status = status
        player.avg = avg
        player.hr = hr
        player.rbi = rbi
        player.wins = wins
        player.losses = losses
        player.era = era
        return player
    
# ---------------------------------------------------------------------

class AtBat(object):
    number = 0
    balls = 0
    strikes = 0
    outs = 0
    pitcher = None
    batter = None
    onFirst = None
    onSecond = None
    onThird = None
    description = ''
    guid = ''

    def make_inning(number, balls, strikes, outs, pitcher, batter, onFirst, onSecond, onThird, description, guid):
        atBat = AtBat()
        atBat.number = number
        atBat.balls = balls
        atBat.strikes = strikes
        atBat.outs = outs
        atBat.pitcher = pitcher
        atBat.batter = batter
        atBat.onFirst = onFirst
        atBat.onSecond = onSecond
        atBat.onThird = onThird
        atBat.description
        atBat.guid = guid

# ---------------------------------------------------------------------

class Pitch(object):
    id = ''
    call = '' # B or S
    callDescription = ''
    speed = 0
    pitchType = ''

    def make_pitch(id, call, callDescription, speed, pitchType):
        pitch = Pitch()
        pitch.id = id
        pitch.call = call
        pitch.callDescription = callDescription
        pitch.speed = speed
        pitch.pitchType = pitchType
    
# ---------------------------------------------------------------------
