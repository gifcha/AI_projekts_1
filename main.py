import random as rd
from gui import start_game
from heur_func import heuristic_function
from gametree import createGameTree

# GUI funkcija
# start_game()

# Skaitļu virkne
defaultLine = ""
lineLength = int(input("Choos a number between form 15 till 25 : "))
for x in range(0,lineLength):
    a = rd.randint(1,9)
    defaultLine = defaultLine + str(a)

print(defaultLine)

# Šeit vajag funkciju kura ģenerēs koku

# Šeit vajag ciklu kurš katru virsotni ar iesūtīs funkcijā "heuristic_function()" un tā piešķirs virsotnei svaru