class Minimax_Node:
  def __init__(self, val, mv, spc):
    self.move = mv
    self.score = val
    self.special = spc
    self.open = True
    self.childs = []
    
  def addChild(self,otherNode):
  	self.childs.append(otherNode)

  def isOpen(self):
    return self.open
  
  def seal(self):
    self.open = False

  def getMove(self):
    return self.move

  def getScore(self):
    return self.score

  def getSpecial(self):
    return self.special

  def getChilds(self):
    return self.childs

  def orderChilds(self):
    self.childs = (sorted(self.getChilds(), key=lambda sim: sim.getData()))

  def clearChilds(self):
    self.childs = []

  def showTree(self,depth):
    s = ''
    s += '{} {}-{}-{} : {}\n'.format(' '*depth, depth, self.getMove(), self.getSpecial(), self.getData())
    for child in self.childs:
        s += child.showTree(depth+1)
    return s

class Minimax_Move:

  def __init__(self, external, score=None):
    self.external = external
    self.score = None

  def getExternal(self):
    return self.external

  def getScore(self):
    return self.score

  def setScore(self):
    self.score = score

  def isScoreDefined(self):
    if self.score == None:
        return False
    return True







# Parameters (can be overridden)
runID = '1'
maxDepth = 4
useZobrist = True
memory_transposition_table = {
    'TEST': 6
}

# Functions to override/replace /!\

def randScore():
    # Depends on the game
    return

def getLegalsMoves():
    # Depends on the game
    return

def getZobristKey():
    # Depends on the game
    return

def Simulator_push(move):
    # Simulate the move
    return

def Simulator_pop():
    # Cancel the last move
    return

# 




def minimax_tree(_head,_depth,_max,_alpha,_beta):

    # Zobrist hashing
    if useZobrist:
        # Get board hash
        actualZobristKey = getZobristKey()
        if actualZobristKey in memory_transposition_table:
            nodeStaticScore = memory_transposition_table[actualZobristKey]
            return nodeStaticScore
    
    if _depth == maxDepth:

        if move.getScore() == None:
            # get move score
            move.setScore(randScore())
        
        return move.getScore()
    
    else:

        # Get _head moves:
        moves = getLegalsMoves()

        if _max:
            maxScore = float('-inf')
            for move in moves:
                Simulator_push(move)
                score = minimax_tree(move,(_depth+1),False,_alpha,_beta)
                Simulator_pop()
                _alpha = max(_alpha, score)
                if _beta <= _alpha:
                    break

            # Save position in Zobrist's transposition table
            if useZobrist:
                ZobristKey = getZobristKey()
                transposition[getZobristKey] = maxScore
                
            return maxScore
        else:
            minScore = float('inf')
            for move in moves:
                Simulator_push(move)
                score = minimax_tree(move,(_depth+1),True,_alpha,_beta)
                Simulator_pop()
                _beta = max(_beta, score)
                if _beta <= _alpha:
                    break

            # Save position in Zobrist's transposition table
            if useZobrist:
                ZobristKey = getZobristKey()
                transposition[getZobristKey] = minScore

            return minScore
        

def saveTranspositionTable():
    f = open("Transposition_Tables/"+runID+".txt", "a")
    f.write(str(memory_transposition_table))
    f.close()
