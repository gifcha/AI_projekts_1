import random as rd

defaultLine = ""
lineLength = int(input("Choos a number between form 15 till 25 : "))
for x in range(0,lineLength):
    a = rd.randint(1,9)
    defaultLine = defaultLine + str(a)

print(defaultLine)
