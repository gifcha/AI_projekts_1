
class node:
    connectedNodes = []
    value: list[int] = []

    def __init__(self, value: list[int]):
        self.value = value

    def addChildNode(self, node):
        self.connectedNodes.append(node)



def createGameTree(value: list[int]):
    root = node(value)
    # add all states using addChildNode(node(statevalue))
