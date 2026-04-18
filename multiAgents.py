import random
import util
from game import Agent

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.
        """
        return self.minimax(gameState, 0, 0)[0]

    def minimax(self, gameState, agentIndex, depth):
        if depth == self.depth or gameState.isWin() or gameState.isLose():
            return None, self.evaluationFunction(gameState)

        if agentIndex == 0:  # Maximizer (Pacman)
            return self.maxValue(gameState, agentIndex, depth)
        else:  # Minimizer (Ghosts)
            return self.minValue(gameState, agentIndex, depth)

    def maxValue(self, gameState, agentIndex, depth):
        bestAction = None
        v = float('-inf')
        for action in gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            _, score = self.minimax(successor, 1, depth)
            if score > v:
                v = score
                bestAction = action
        return bestAction, v

    def minValue(self, gameState, agentIndex, depth):
        bestAction = None
        v = float('inf')
        numAgents = gameState.getNumAgents()
        nextAgent = agentIndex + 1
        nextDepth = depth
        if nextAgent == numAgents:
            nextAgent = 0
            nextDepth += 1

        for action in gameState.getLegalActions(agentIndex):
            successor = gameState.generateSuccessor(agentIndex, action)
            _, score = self.minimax(successor, nextAgent, nextDepth)
            if score < v:
                v = score
                bestAction = action
        return bestAction, v

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.
    """
    def getAction(self, gameState):
        legalActions = gameState.getLegalActions()
        scores = [self.evaluationFunction(gameState, action) for action in legalActions]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)
        return legalActions[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        successorGameState = currentGameState.generateSuccessor(0, action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()

        score = successorGameState.getScore()
        foodList = newFood.asList()

        if foodList:
            minFoodDist = min([util.manhattanDistance(newPos, food) for food in foodList])
            score += 10.0 / minFoodDist

        for ghostState in newGhostStates:
            ghostDist = util.manhattanDistance(newPos, ghostState.getPosition())
            if ghostDist > 0:
                if ghostState.scaredTimer > 0:
                    score += 200.0 / ghostDist
                else:
                    score -= 10.0 / ghostDist

        return score
