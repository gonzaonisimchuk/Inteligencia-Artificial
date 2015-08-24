#from simpleai.search import (SearchProblem, breadth_first, depth_first,
                             #iterative_limited_depth_first, greedy,
                             #astar)
from simpleai.search import SearchProblem, breadth_first, depth_first, astar, greedy, limited_depth_first
from simpleai.search.viewers import WebViewer, ConsoleViewer, BaseViewer


#GOAL = (
    #(4, 0),
    #(2, 2),
    #(0, 4),
#)

INITIAL = (
    (4, 0),
    (2, 2),
    (0, 4),
) # 0 heroe, 0 < enemigos
lMat = 2
nMatriz = 4 #5 - 1

def find_number(board, number):
    for row_index, row in enumerate(board):
        for col_index, current_number in enumerate(row):
            if current_number == number:
                return row_index, col_index


def find_element(board, number):
    row = board[number][0]
    col = board[number][1]
    return row, col


def isEnem(board, row, col):
    tup = (row, col)
    for ntup in board:
        if ntup == tup:
            return ntup
    return None


def find_action(action):
    row = action[0]
    col = action[1]
    enem = action[2]
    return row, col, enem


class entrega1tradicional(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        return len(state) == 1

    def actions(self, state):
        row_0, col_0 = find_element(state, 0)
        actions = []

        if row_0 > 0:
            actions.append((row_0 - 1, col_0, isEnem(state, row_0 - 1, col_0)))
        if row_0 < nMatriz:
            actions.append((row_0 + 1, col_0, isEnem(state, row_0 + 1, col_0)))
        if col_0 > 0:
            actions.append((row_0, col_0 - 1, isEnem(state, row_0, col_0 - 1)))
        if col_0 < nMatriz:
            actions.append((row_0, col_0 + 1, isEnem(state, row_0, col_0 + 1)))

        return actions

    def result(self, state, action):
        state_modificable = [list(row) for row in state]

        row_0, col_0, enem = find_action(action)

        if enem != None:
            state_modificable.remove(enem)
        else:
            state_modificable[0] = (row_0, col_0)
        #state_modificable = action
        #state_modificable[row_0][col_0] = action
        #state_modificable[row_a][col_a] = 0

        return tuple(tuple(row) for row in state_modificable)

    #def heuristic(self, state):
        #total_difference = 0
        #for row_index, row in enumerate(state):
            #for col_index, current_number in enumerate(row):
                #row_goal, col_goal = find_number(GOAL, current_number)
                #difference = abs(row_index - row_goal) + abs(col_index - col_goal)
                #total_difference += difference
        #return total_difference


def resolver(metodo_busqueda):
    visor = BaseViewer()
    if metodo_busqueda == 'breadth_first': #Amplitud
        result = breadth_first(entrega1tradicional(INITIAL),viewer=visor, graph_search=True)
    elif metodo_busqueda == 'depth_first': #Profundidad
        result = depth_first(entrega1tradicional(INITIAL),viewer=visor, graph_search=True)
    elif metodo_busqueda == 'limited_depth_first': # Profundidad Limitada
        result = limited_depth_first(entrega1tradicional(INITIAL), 10, graph_search=True,viewer=visor)
    elif metodo_busqueda == 'greedy': #Avara
        result = greedy(entrega1tradicional(INITIAL),viewer=visor, graph_search=True)
    elif metodo_busqueda == 'astar':#A*
        result = astar(entrega1tradicional(INITIAL),viewer=visor, graph_search=True)

    return result