playerFirstMove = False

class node:
    connectedNodes = []
    playerPoints: int = 0
    aiPoints: int = 0
    value: list[int] = []

    def __init__(self, value: list[int], playerPoints, aiPoints):
        self.value = value
        self.playerPoints = playerPoints
        self.aiPoints = aiPoints

    def addChildNode(self, node):
        self.connectedNodes.append(node)



# not finished 
def createGameTree(value: list[int]):
    root = node(value, 0, 0)
    currentNode = root
    isPlayerMove: bool = playerFirstMove

    while(len(currentNode.value) > 1):
        isPlayerMove = not isPlayerMove

        for i in range(len(currentNode.value) - 1):
            newValue = currentNode.value
            pairSum = newValue.pop(i) + newValue.pop(i)

            replaceNum: int = 1
            pointsToAdd: int = 0
            if pairSum == 7:
                replaceNum = 2
                points += 1
            elif pairSum < 7:
                replaceNum = 3
                points += -1
            pointsToAdd = 1;

            newValue.insert(i, replaceNum)

            aiP: int = 0
            plP: int = 0

            # aiP = currentNode.aiPoints + (pointsToAdd * (not playerFirstMove)) # if (not playerFirstMove) is false result is 0
            # plP = currentNode.playerPoints + (pointsToAdd * playerFirstMove)
            currentNode.addChildNode(node(newValue, aiP, plP))
    
    # add all states using addChildNode(node(statevalue, playerPoints, aiPoints))