# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from game import Directions

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]
    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #isVisited = {}
    #currentState = problem.getStartState()
    #if problem.isGoalState(currentState[0]):
    #    return []
    #path = []
    #for successor in problem.getSuccessors(currentState):
    #    if successor[0] == currentState[0]:
    #        continue
    #    success, directions = dfsRecursive(problem, successor)
    #    if success:
    #        path += directions
    #print path   
    #return path

    expanded = {}
    deadEnd = {}
    path = []
    stateStack = util.Stack()

    currentState = problem.getStartState()
    stateStack.push((currentState, None, 1))
    backtrackOutOfLoop = 0
    isBackTracking = False
    while not stateStack.isEmpty():
        #print(path)
        currentState = stateStack.pop()
        expanded[currentState[0]] = True
        if isBackTracking:
            del path[-1]
            isBackTracking = False
        else:
            path.append(currentState[0])
        successors = problem.getSuccessors(currentState[0])
       
        successors = [x for x in successors if not deadEnd.has_key(x[0])]

        # check if goal state
        if problem.isGoalState(currentState[0]):
            return path[1:]

        # Check if dead end.
        # Dead end if len(successors) == 1 && not goal
        # All successors are dead ends
        if len(successors) == 1 and expanded.has_key(successors[0][0]):
            # this is dead end.
            #print("\nis in dead end\n")
            deadEnd[currentState[0]] = True
            stateStack.push(successors[0])
            isBackTracking = True
            continue

        allExpandedOrDeadEnds = True
        for successor in problem.getSuccessors(currentState[0]):
            if deadEnd.has_key(successor[0]) or expanded.has_key(successor[0]):
                continue
            stateStack.push(successor)
            allExpandedOrDeadEnds = False
        #allExpandedOrDeadEnds means we are dealing with a loop
        if allExpandedOrDeadEnds:
            backtrackOutOfLoop = backtrackOutOfLoop+1
            deadEnd[currentState[0]] = True
            successor = [x for x in successors if x[1] == Directions.REVERSE[path[-backtrackOutOfLoop]]][0]
            isBackTracking = True
            stateStack.push(successor)
        else:
            backtrackOutOfLoop = 0
           

        
             

isVisited = {}
def dfsRecursive(problem, node) :
    isVisited[node[0]] = True
    path = [node[1]]
    if node[0] == None:
        return (False, path)
    if problem.isGoalState(node[0]):
        return (True, path)
    if len(problem.getSuccessors(node[0])) == 0:
        return (False, path)

    for successor in problem.getSuccessors(node[0]):
        if successor[0] in isVisited:
            continue
        success, directions = dfsRecursive(problem, successor)
        if success:
            return (success, path + directions)

    return False, path

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    expanded = {}
    deadEnd = {}
    path = []
    stateStack = util.Stack()

    currentState = problem.getStartState()
    stateStack.push((currentState, None, 1))
    backtrackOutOfLoop = 0
    isBackTracking = False
    while not stateStack.isEmpty():
        #print(path)
        currentState = stateStack.pop()
        expanded[currentState[0]] = True
        if isBackTracking:
            del path[-1]
            isBackTracking = False
        else:
            path.append(currentState[1])
        successors = problem.getSuccessors(currentState[0])
       
        successors = [x for x in successors if not deadEnd.has_key(x[0])]

        # check if goal state
        if problem.isGoalState(currentState[0]):
            return path[1:]

        # Check if dead end.
        # Dead end if len(successors) == 1 && not goal
        # All successors are dead ends
        if len(successors) == 1 and expanded.has_key(successors[0][0]):
            # this is dead end.
            #print("\nis in dead end\n")
            deadEnd[currentState[0]] = True
            stateStack.push(successors[0])
            isBackTracking = True
            continue

        allExpandedOrDeadEnds = True
        for successor in problem.getSuccessors(currentState[0]):
            if deadEnd.has_key(successor[0]) or expanded.has_key(successor[0]):
                continue
            stateStack.push(successor)
            allExpandedOrDeadEnds = False
        #allExpandedOrDeadEnds means we are dealing with a loop
        if allExpandedOrDeadEnds:
            backtrackOutOfLoop = backtrackOutOfLoop+1
            deadEnd[currentState[0]] = True
            successor = [x for x in successors if x[1] == Directions.REVERSE[path[-backtrackOutOfLoop]]][0]
            isBackTracking = True
            stateStack.push(successor)
        else:
            backtrackOutOfLoop = 0
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch