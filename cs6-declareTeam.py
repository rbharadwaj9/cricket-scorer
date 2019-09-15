# Cricket Scorer
# First try to make it work in terminal
import warnings
from sys import exit

# import numpy as np

# ***** TEAM CLASS *****
# The team class contains batsmen and team name


class Team:
    def __init__(self, team_name, teamSize):
        self.team_name = team_name
        self.players = [None]*teamSize  # Declare outside.
        self.playersName = [None]*teamSize
        self.team_score = 0
        self.deadBatsmen = []
        # self.strike = [[None,True],[None,False]] #Each element will have two
        # dimensions: Batsman and strike situation.

    def selectBatsmen(self, batsman1, batsman2):
        self.strike[0] = batsman1
        self.strike[1] = batsman2

    def teamScore(self, runs):
        self.team_score += runs

# ***** BATSMAN CLASS *****


class Batsman(Team):
    strikeChange = False
    # Batsman has number of runs, number of balls, number of fours,
    # number of sixes, strike rate.

    def __init__(self, player_name):  # At Initialisation
        self.name = str(player_name)

        self.runs = 0
        self.balls = 0
        self.fours = 0
        self.sixes = 0
        self.sr = 0
        self.wicket = False

    def playBall(self, runs, extras):
        if runs > 6:
            warnings.warn("Runs must not exceed 6. Idiot!")
        elif extras is True:
            t1.teamScore(runs)
        else:
            # Score Runs
            self.runs += runs
            self.balls += 1
            self.sr = (self.runs/self.balls)*100
            t1.teamScore(runs)  # t1 will change to currentTeam
            if runs == 4:
                self.fours += 1
            elif runs == 6:
                self.sixes += 1

    def printStatistics(self):
        print('Batsman Name:', self.name)
        print('Runs Scored:', self.runs)
        print('Balls Played:', self.balls)
        print('Number of Fours:', self.fours)
        print('Number of Sixes:', self.sixes)
        print("Strike Rare:", self.sr)
        print("************")

# ***** ENTER TEAM DETAILS *****


def declareTeam():
    # Input two team names t1,t2
    # Input number of players per team
    # create array of players inside each.
    # each batsman instead of being b1, will be players[1]
    teamSize = int(input("How many players per team?"))
    t1 = Team(input("Team 1 name:"), teamSize)
    t2 = Team(input("Team 2 name:"), teamSize)

    print("Details of Team 1:")
    for i in range(0, teamSize):
        t1.players[i] = Batsman(input("Player "+str(i+1)+"'s name:"))
        t1.playersName[i] = t1.players[i].name

    print("Details of Team 2:")
    for i in range(0, teamSize):
        t2.players[i] = Batsman(input("Player "+str(i+1)+"'s name:"))
        t2.playersName[i] = t2.players[i].name

    print(t1.players, t1.playersName)
    print(t2.players, t2.playersName)

    strike = [[t1.players[0], True],
              [t1.players[1], False]]  # Afterwards we can choose - on strike.
    return t1, t2, strike


def currentStrike(strike):  # Returns who is on strike.
    if strike[0][1] is True:
        onStrike = 0
        nonStrike = 1
    elif strike[1][1] is True:
        onStrike = 1
        nonStrike = 0
    return onStrike, nonStrike

# ***** MAIN FUNCTION FOR THE NEXT BALL *****


# Our action goes through this so that I can add wide, No ball and everything.
# Each action will come under an elif.
def nextBall(action, strike):
    onStrike, nonStrike = currentStrike(strike)
    currentBatsman = strike[onStrike][0]
    print("Batsman on strike is", currentBatsman.name)

    if action == 'W':
        print("***WICKET***")
        currentBatsman.printStatistics()
        strike = afterWicket(currentBatsman)
    elif action == "Wd":
        currentBatsman.playBall(1, True)
        pass  # Wide Ball
    elif action == "Nb":
        currentBatsman.playBall(1, True)
        pass  # No ball
    elif action == "EXIT":
        exit()
    else:
        runs = int(action)
        print(runs, "runs.")
        currentBatsman.playBall(runs, False)
        strikeChange(runs, onStrike, nonStrike)


def strikeChange(runs, onStrike, nonStrike):
    # Check Strike
    if runs % 2 == 0:
        # pass
        print("NO STRIKE CHANGE")
    else:
        print("STRIKE CHANGE")
        strike[onStrike][1] = False
        strike[nonStrike][1] = True
        print("New strike", strike)

# ***** SELECT NEW BATSMAN *****


def afterWicket(oldBatsman):
    t1.deadBatsmen.append(oldBatsman)
    for i in t1.playersName:
        print(i)

    batsmanChanged = False

    while batsmanChanged is False:
        newBatter = input("New Batsman Name:")
        for man in t1.deadBatsmen:
            print(man)
            # if newBatter == man:
            # 	print("Enter a Valid Batsman.")
            # 	break
            # else:
            # 	batsmanChanged = True

    batsmanChanged = False

    while batsmanChanged is False:
        for j in range(1, len(t1.playersName)):
            if t1.playersName[j] == newBatter:
                if strike[0][0] == oldBatsman:
                    strike[0][0] = t1.players[j]
                elif strike[1][0] == oldBatsman:
                    strike[1][0] = t1.players[j]
                batsmanChanged = True
        if batsmanChanged is not True:
            print("Enter a valid batsman.")

    print("New Strike:", strike)
    return strike


# ***** PLAY GAME *****
t1, t2, strike = declareTeam()
deadBatsmen = []

try:
    while True:
        nextBall(input("Next Ball?"), strike)
        print("******************")
        print("Team Runs:", t1.team_score)
        print("\n")
except Exception as e:
    print(e)

# ***** THINGS YET TO SORT *****
# During After wicket, you can choose a batsman that has already gotten out.
# We need some array of old batsmen or available batsmen from
# where you can choose.
