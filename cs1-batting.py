# Cricket Scorer
# First try to make it work in terminal
import warnings

# ***** BATSMAN CLASS *****


class batsman:
    # Batsman has number of runs, number of balls, number of fours, number of sixes, strike rate.
    def __init__(self, name):  # At Initialisation
        self.name = str(name)

        self.runs = 0
        self.balls = 0
        self.fours = 0
        self.sixes = 0
        self.sr = 0
        self.wicket = False
        self.strikeChange = False

    def playBall(self, action):
        runs = int(action)
        print("Action: ", runs)

        if runs > 6:
            warnings.warn("Runs must not exceed 6. Idiot!")
        else:
            # Score Runs
            self.runs += runs
            self.balls += 1

            self.sr = (self.runs/self.balls)*100

            if runs == 4:
                self.fours += 1
            elif runs == 6:
                self.sixes += 1

            # Check Strike
            if runs % 2 == 0:
                self.strikeChange = False
            else:
                self.strikeChange = True

    def printStatistics(self):
        print('Batsman Name:', self.name)
        print('Runs Scored:', self.runs)
        print('Balls Played:', self.balls)
        print('Number of Fours:', self.fours)
        print('Number of Sixes:', self.sixes)
        print("Strike Rare:", self.sr)


b1 = batsman('Gayle')

while True:
    bat_action = input("How many runs? ")
    print("\n")

    if bat_action == 'W':
        print("AND ", b1.name, "IS OUT!!")
        b1.wicket = True
        b1.printStatistics()
        break

    else:
        b1.playBall(bat_action)
        print("Runs:", b1.runs, " Balls:", b1.balls, " Fours:", b1.fours, " Sixes:",
              b1.sixes, " Strike Change?", b1.strikeChange, "Strike Rate", b1.sr)
        print("*****NEXT BALL*****")

    print("\n")
