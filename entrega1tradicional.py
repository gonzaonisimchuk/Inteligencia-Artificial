from simpleai.search import SearchProblem, breadth_first, depth_first, astar, greedy, iterative_limited_depth_first
from simpleai.search.viewers import BaseViewer

INITIAL = (
    (0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0),
    (0, 0, 0, 0, 0),
    (2, 0, 0, 0, 0),
)

nMatriz = 4 #5 - 1


def find_number(board, number):
    for row_index, row in reversed(list(enumerate(board))):
        for col_index, current_number in enumerate(row):
            if current_number == number:
                return row_index, col_index


def count_number(board, number):
    i = 0
    for row_index, row in reversed(list(enumerate(board))):
        for col_index, current_number in enumerate(row):
            if current_number == number:
                i += 1
    return i

# def find_element(board, number):
    # row = board[number][0]
    # col = board[number][1]
    # return row, col


# def isEnem(board, row, col):
    # tup = (row, col)
    # for ntup in board:
        # if ntup == tup:
            # return ntup
    # return None


# def find_action(action):
    # row = action[0]
    # col = action[1]
    # enem = action[2]
    # return row, col, enem	


class entrega1tradicional(SearchProblem):
    def cost(self, state1, action, state2):
        return 1

    def is_goal(self, state):
        count = count_number(state, 1)
        return count == 0

    def actions(self, state):
        row_0, col_0 = find_number(state, 2)
        actions = []

        if row_0 > 0:
            actions.append([row_0 - 1, col_0])
        if row_0 < nMatriz:
            actions.append([row_0 + 1, col_0])
        if col_0 > 0:
            actions.append([row_0, col_0 - 1])
        if col_0 < nMatriz:
            actions.append([row_0, col_0 + 1])

        return actions

    def result(self, state, action):
        state_modificable = [list(row) for row in state]
        row_a, col_a = action[0], action[1]

        if (state_modificable[row_a][col_a]) == 1:
            state_modificable[row_a][col_a] = 0
        else:
            state_modificable[row_a][col_a] = 2
            row_0, col_0 = find_number(state, 2)
            state_modificable[row_0][col_0] = 0

        return tuple(tuple(row) for row in state_modificable)

    def heuristic(self, state):
        return count_number(state, 1)


def resolver(metodo_busqueda):
    visor = BaseViewer()
    if metodo_busqueda == 'breadth_first':
        result = breadth_first(entrega1tradicional(INITIAL), graph_search=True, viewer=visor)
    if metodo_busqueda == 'depth_first':
        result = depth_first(entrega1tradicional(INITIAL), graph_search=True, viewer=visor)
    if metodo_busqueda == 'limited_depth_first':
        result = iterative_limited_depth_first(entrega1tradicional(INITIAL),10, viewer=visor)
    if metodo_busqueda == 'greedy':
        result = greedy(entrega1tradicional(INITIAL), graph_search=True, viewer=visor)
    if metodo_busqueda == 'astar':
        result = astar(entrega1tradicional(INITIAL), graph_search=True, viewer=visor)

    return result