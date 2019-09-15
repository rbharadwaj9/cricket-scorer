# Cricket Scorer
# First try to make it work in terminal
import warnings

# ***** TEAM CLASS *****
# The team class contains batsmen and team name


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
        self.team_score = 0
        # self.strike = [[None,True],[None,False]] #Each element will have two dimensions: Batsman and strike situation.

    def selectBatsmen(self, batsman1, batsman2):
        self.strike[0] = batsman1
        self.strike[1] = batsman2

    def addPlayer(self, player_id):
        self.players.append(player_id)

    def teamScore(self, runs):
        self.team_score += runs

# ***** BATSMAN CLASS *****


class Batsman(Team):
    strikeChange = False
    # Batsman has number of runs, number of balls, number of fours, number of sixes, strike rate.

    def __init__(self, player_name, ID):  # At Initialisation
        self.team_name = ID
        self.name = str(player_name)
        self.runs = 0
        self.balls = 0
        self.fours = 0
        self.sixes = 0
        self.sr = 0
        self.wicket = False

        self.team_name.addPlayer(self)

    # Our action goes through this so that I can add wide, No ball and everything. Each action will come under an elif.
    def action(self, action):
        if action == 'W':
            print("***WICKET***")
            self.printStatistics()
        elif isinstance(action, int):
            print(action, "runs.")
            self.playBall(action)

    def playBall(self, runs):

        if runs > 6:
            warnings.warn("Runs must not exceed 6. Idiot!")
        else:
            # Score Runs
            self.runs += runs
            self.balls += 1
            self.sr = (self.runs/self.balls)*100

            self.team_name.teamScore(runs)

            if runs == 4:
                self.fours += 1
            elif runs == 6:
                self.sixes += 1

            # Check Strike
            if runs % 2 == 0:
                strikeChange = False
            else:
                strikeChange = True

    def printStatistics(self):
        print('Batsman Name:', self.name)
        print('Runs Scored:', self.runs)
        print('Balls Played:', self.balls)
        print('Number of Fours:', self.fours)
        print('Number of Sixes:', self.sixes)
        print("Strike Rare:", self.sr)
        print("************")


def currentStrike(strike):  # Returns who is on strike.
    strike = strike
    if strike[0][1] is True:
        onStrike = 0
        nonStrike = 1
    elif strike[1][1] is True:
        onStrike = 1
        nonStrike = 0


# Def play ball (Action). Find out who is on strike and then do batsmen.action()
t1 = Team("RCB")
t2 = Team("CSK")

b1 = Batsman('Gayle', t1)
b2 = Batsman('Kohli', t1)
b3 = Batsman('DeVillers', t1)

b4 = Batsman('Dhoni', t2)
b5 = Batsman("Raina", t2)
b6 = Batsman("Jadeja", t2)

t1.selectBatsmen([b1, True],
                 [b2, False])
print(t1.strike[0][1])
b1.action(4)
b1.action(4)
b1.action(4)
b1.action('W')
# print(t1.players)
print("Team Runs:", t1.team_score)
