import random as rd
#from gui import start_game
from heur_func import heuristic_function
#from gametree import createGameTree

# GUI funkcija
# start_game()

# Skaitļu virknes ģenerēšana
startString = []
lineLength = int(input("Choos a number between form 15 till 25 : "))
for x in range(0,lineLength):
    a = rd.randint(1,9)
    startString.append(a)

#Sākuma nosacījums
playerScore = 0
aiScore = 0

# heuristic_function() izmantošana : 
stateValue = heuristic_function(startString, playerScore, aiScore)
print(stateValue)