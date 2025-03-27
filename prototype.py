import math
import random
import datetime


# Mezgls saistītā sarakstā
class rindANode:
    def __init__(self, value) -> None:
        self.value = value # Mezglā saglabātā vērtība. 
        self.next = None # saite uz nākamo mezgli 
        self.prev = None # saite uz iepriekšējo mezgli
        
# saistīts saraksts
class rindA:
    def __init__(self):
        self.front = None # Norāda uz pirmo mezglu rinda
        self.back = None # Norāda uz pēdējo mezglu rinda
        self.size = 0 # Izseko Mezgļu skaitu rinda

    # pievienot Node rindai(saistītā sarakstā) aizmugurei
    def append(self, value):
        new_node = rindANode(value) # Izveidot jaunu mezgli ar vērtību value
        if not self.back: #  ja rinda ir tukša gan priekšpuse, gan aizmugure norāda uz jauno mezglu
            self.front = self.back = new_node
        else: 
            self.back.next = new_node # Iestatiet nākamo no pašreizējā aizmugurējā mezgla uz jauno mezglu
            new_node.prev = self.back # Iestatīt mezgla iepriekšējo uz pašreizējo aizmugurējo mezglu
            self.back = new_node # Atjauniniet rādītāju uz jauno mezglu
        self.size += 1 # Palielināt mezglu skaititaju par 1

    def popleft(self): #Noņem un atgriež elementu value no rindai priekšpuses
        if not self.front:  # Pārbaudiet, vai rinda ir tukša,atgriezt None ja jā
            return None

        value = self.front.value # Saglabājiet priekšējā mezgla vērtību
        self.front = self.front.next # Pārvietojiet rādītāju uz nākamo mezglu
        if self.front: # Ja ir jauns mezgls priekšpuse, iestatiet iepriekšējo rādītāju uz None
            self.front.prev = None
        else:
            self.back = None  # Ja rind kļūst tukša iestatiet iepriekšējo rādītāju uz None
        self.size -= 1 # samazināt mezglu skaitītāju par 1
        return value

    def extend(self, values): # Pievienojiet katru vērtību rindai aizmugurē
        for value in values:
            self.append(value)

    def __len__(self): # Atgriezt pašreizējo rindu lielumu
        return self.size


# Datu struktūra paša koka saglabāšanai
class Node:
    #spēles stavokļis - viena virsotne kokam
    def __init__(self, value : list[int], aiPoints : int, playerPoints : int, parent=None) -> None:
        self.value = value # spēles stavokļa virkne, piem [3,4,5,6,7]
        self.aiPoints = aiPoints # punktu skaits mākslīgajam inteliģentam
        self.playerPoints = playerPoints # Spēlētāja pašreizējais punktu skaits 
        self.children = [] # Saglabā pectečus 
        self.parents = []  # Saglabā priekštečus dublikātu novirzīšanai
        self.parent = parent  # Saite uz riekšteču
    
    # Stavokļu pēcteču pievienošana
    def addChildNode(self, child) -> None:
        self.children.append(child) # Pievienot priekšteču stavokļa priekštečus kopai
        child.parents.append(self) # Pievienot pēcteci stavokļa pecteču kopai
 
    # Izvadei ārpus klases TEMP!!
    def __repr__(self) -> str:
        return f"Stavokļis({self.value}, AI: {self.aiPoints}, Player: {self.playerPoints})"

# speles koka izveide. Value: pašreizeja stavokļā skaitļu virkne piem [1,5,4,3,2] 
def createGameTree(value: list[int], aiPoints: int, playerPoints: int, playerFirstMove: bool, max_depth: int):
    root = Node(value, aiPoints, playerPoints) # speles koka saknes izveidošana 
    queue = rindA() # konstruktora izsaukšana rindai
    queue.append((root, 0, playerFirstMove)) # dziļuma izsekošana un pašreizējais spēlētājs kas veic gājienu
    #print(queue) DEBUG
    stateMap = {} # visu stavokļu saglabāšana
    stateMap[(tuple(value), aiPoints, playerPoints)] = root # pievienojot sakni kā pirmo sākuma pozīciju
    
    isPlayerMove = playerFirstMove # lietota DEBUG var var noņemt

    
    
    while len(queue) > 0:
        currentNode, level, isPlayerMove = queue.popleft() #Noņemt no rindas un iegūstiet pašreizējo pozīciju, dziļumu, pašreizējo spēlētāju
        if level >= max_depth:  # apstāties, sasniedzot maksimālo dziļumu
            continue

        for i in range(len(currentNode.value) - 1):
            #Visu pecteçu iegūšana no pašreizēja stavokļa
            pairSum = currentNode.value[i] + currentNode.value[i + 1] # divu tuvu skaitļu pāra summa
            replaceNum = 0 # vērtība, kurai pāris tiks aizvietots
            aiP, plP = currentNode.aiPoints, currentNode.playerPoints # iegūt punktus no abiem pašreizējā stavokļa spēlētājiem
            
            #Punktu sadalijums atbilstoši spēles noteikumiem
            if pairSum == 7:
                replaceNum = 2
                plP += 1
                aiP += 1 
                    
            elif pairSum < 7:
                replaceNum = 3
                if isPlayerMove:
                    aiP -= 1 
                else:
                    plP -= 1  
            else:
                replaceNum = 1
                if isPlayerMove:
                    plP += 1 
                else:
                    aiP += 1
      

            newState = currentNode.value[:]  # Izveido value kopiju
            newState[i] = replaceNum  # aizstāt elementu  i
            del newState[i + 1]  # dzēš elementu i + 1
            
            stateTuple = (tuple(newState), aiP, plP) # jauns stavokļis
            
            # Pārbauda, vai virsotnes dublikāts pastāv, ja jā saskaņā ar spēles koka nosacījumu novirza pašreizējo virsotni uz jau esošu
            if stateTuple in stateMap:
                existing_node = stateMap[stateTuple]
                currentNode.addChildNode(existing_node)
            # ja virsotne ir unikāla, pievieno kokam kā atsevišķu virsotni
            else:
                new_node = Node(newState, aiP, plP)
                stateMap[stateTuple] = new_node
                currentNode.addChildNode(new_node)
                queue.append((new_node, level + 1,not isPlayerMove)) #Pāreja uz nākamo dziļumu, spēlētāja maiņa
    print(stateMap) # visu stavokļu saglabāšana print
    return root

# NEED FIX!!!
def heuristic(node):
    

    N1, N2, N3 = 0, 0, 0  # Skaita dažādu veidu gājienus
        
    for i in range(len(node.value) - 1):
        pair_sum = node.value[i] + node.value[i + 1]
        if pair_sum > 7:
            N1 += 1  # Labvēlīgs solis AI
        elif pair_sum < 7:
            N2 += 1  # Var samazināt pretinieka punktu skaitu
        else:  # pair_sum == 7
            N3 += 1  # Neitrāls gājiens, kas dod punktus abiem spēlētājiem
        
    # Heiristisko komponentu svari
    w1 = 2.0  # Svars labām gajienam (summa > 7)
    w2 = 1.0  # Svars pretinieku samazināšanas gājieniem (summa < 7)
    w3 = 0.2  # Svars neitrālām kustībām (summa == 7)
    w4 = 2.0  # Svars vērtību 
    w5 = 2.0  # Svars vērtību 
    
    # Heiristisko vērtību apreķināšana
    if (node.aiPoints - node.playerPoints) == 0:
        H = (w4 * (1)) + (w1 * N1) + (w2 * N2) + (w3 * N3)
    else:
        H = (w5 * node.aiPoints) * (w4 * (node.aiPoints - node.playerPoints)) + (w1 * N1) + (w2 * N2) + (w3 * N3)
        #print(H)
    return H


# Minimax/Alpha|Beta algoritms, vajag testēt  
def minimax(node, depth, isMaximizingPlayer, alpha=None, beta=None):
    if depth == 0 or not node.children:
        return heuristic(node)

    if alpha is None or beta is None:
        if isMaximizingPlayer:
            maxEval = -math.inf
            for child in node.children:
                eval = minimax(child, depth - 1, False)
                maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = math.inf
            for child in node.children:
                eval = minimax(child, depth - 1, True)
                minEval = min(minEval, eval)
            return minEval
    else:
        if isMaximizingPlayer:
            maxEval = -math.inf
            for child in node.children:
                eval = minimax(child, depth - 1, False, alpha, beta)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break 
            return maxEval
        else:
            minEval = math.inf
            for child in node.children:
                eval = minimax(child, depth - 1, True, alpha, beta)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  
            return minEval

# Algoritms labāka AI novietojuma izvēlei
def selectBestMove(root, depth, maximize=True, alphaBeta=True):
    if maximize:
        bestValue = -math.inf
    else:
        bestValue = math.inf
    bestMove = None
    
    for childNode in root.children:
        if alphaBeta:
            moveValueUp = minimax(childNode, depth - 1, not maximize,-math.inf, math.inf)
        else:
            moveValueUp = minimax(childNode, depth - 1, not maximize)

        if maximize:
            if moveValueUp > bestValue:
                bestValue = moveValueUp
                bestMove = childNode
        else:
            if moveValueUp < bestValue:
                bestValue = moveValueUp
                bestMove = childNode
    return bestMove


# TIKAI TESTAM!!!
def play_game(initial_values, n_layers, useAlphaBeta=True):
    aiPoints = 0
    playerPoints = 0
    CurrentPos = createGameTree(initial_values, aiPoints, playerPoints,playerFirstMove=True, max_depth=n_layers)
    posVirkne = [CurrentPos] 

    if len(CurrentPos.children) == 0:
        return 

    while True:
        print("\nCurrent State:", CurrentPos.value)
        print(f"Points -> AI: {CurrentPos.aiPoints}, Player: {CurrentPos.playerPoints}")

        if len(CurrentPos.children) == 0: 
            print(posVirkne) # Viss ceļš
            break

        movIndex = int(input("Select index: "))
        if movIndex < 0 or movIndex >= len(CurrentPos.children):
            continue

        CurrentPos = CurrentPos.children[movIndex]
        posVirkne.append(CurrentPos) 

        CurrentPos = createGameTree(CurrentPos.value, CurrentPos.aiPoints,CurrentPos.playerPoints,playerFirstMove=False, max_depth=n_layers)

        if len(CurrentPos.children) == 0:
            for x in posVirkne:
                print(x) # Viss ceļš
            break


        CurrentPos = selectBestMove(CurrentPos, depth=n_layers, maximize=True, alphaBeta=useAlphaBeta)
        posVirkne.append(CurrentPos)  
        
        
    
# Piemers
data = []
for _ in range(10):
    data.append(random.randint(1, 9))
a = datetime.datetime.now()
play_game([7, 5, 4, 3, 8, 8, 3, 6, 5, 5], n_layers=5, useAlphaBeta=True) # vajag testet vai ģenerācija darbojas pareizi
b = datetime.datetime.now()
print(b-a)


        


