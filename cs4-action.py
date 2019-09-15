#Cricket Scorer
#First try to make it work in terminal
import warnings
import numpy as np

# ***** TEAM CLASS *****
#The team class contains batsmen and team name
class Team:
	def __init__(self, team_name):
		self.team_name = team_name
		self.players = []
		self.team_score = 0
		#self.strike = [[None,True],[None,False]] #Each element will have two dimensions: Batsman and strike situation.

	def selectBatsmen(self,batsman1,batsman2):
		self.strike[0] = batsman1
		self.strike[1] = batsman2


	def addPlayer(self, player_id):
		self.players.append(player_id)

	def teamScore(self,runs):
		self.team_score += runs

# ***** BATSMAN CLASS *****
class Batsman():
	strikeChange = False
	# Batsman has number of runs, number of balls, number of fours, number of sixes, strike rate.
	def __init__(self,player_name,ID): #At Initialisation 
		self.team_name = ID
		self.name = str(player_name)
		self.runs = 0
		self.balls = 0
		self.fours = 0
		self.sixes = 0
		self.sr = 0
		self.wicket = False

		self.team_name.addPlayer(self)
 
	def playBall(self,runs):

		if runs > 6:
			warnings.warn("Runs must not exceed 6. Idiot!")
		else:
			#Score Runs
			self.runs += runs
			self.balls += 1
			self.sr = (self.runs/self.balls)*100

			self.team_name.teamScore(runs)
			
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
	
def currentStrike(strike): #Returns who is on strike.
	#strike = [[b1,True],[b2, False]] 
	if strike[0][1] == True:
		onStrike = 0
		nonStrike = 1 
	elif strike[1][1] == True:
		onStrike = 1
		nonStrike = 0
	return onStrike,nonStrike

#Def play ball (Action). Find out who is on strike and then do batsmen.action()
def nextBall(action,strike): #Our action goes through this so that I can add wide, No ball and everything. Each action will come under an elif.
	onStrike,nonStrike = currentStrike(strike)
	currentBatsman = strike[onStrike][0]
	print(type(currentBatsman))
	print("Batsman on strike is", currentBatsman.name)

	if isinstance(action,int):
		print(action, "runs.")
		currentBatsman.playBall(action)
	elif action == 'W':
		print("***WICKET***")
		currentBatsman.printStatistics()
	elif action == "Wd":
		pass #Wide Ball
	elif action == "Nb":
		pass #No ball
	print("Strike Change:",strikeChange(action))
	if strikeChange(action) == True:
		strike[onStrike][1] = False
		strike[nonStrike][1] = True
	print("new Strike",strike)

def strikeChange(runs):
	#Check Strike
	if runs % 2 == 0:
		return False
	else:
		return True
#Steps after Wicket 
#********
#Input new Batsman
#save as new object and then replace old batsman in strike array.
#Ask if strike will change


#Declare Teams and Batsmen
t1 = Team("RCB")
t2 = Team("CSK")

b1 = Batsman('Gayle',t1)
b2 = Batsman('Kohli',t1)
b3 = Batsman('DeVillers',t1)

b4 = Batsman('Dhoni',t2)
b5 = Batsman("Raina",t2)
b6 = Batsman("Jadeja",t2)
#Play Game
strike = [[b1,True],
			[b2,False]]

nextBall(4,strike)
print("******************")
print("\n")
nextBall(3,strike)
print("******************")
print("\n")
nextBall(1,strike)
print("******************")
print("\n")


#print(t1.players)
print("Team Runs:",t1.team_score)