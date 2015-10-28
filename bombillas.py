# coding: utf-8
#El problema de las bombillas consiste en apagar todas las bombillas del tablero, a
#partir de una configuraci´on inicial aleatoria. Para conseguir esto, es posible seleccionar
#un bombilla y mudar su estado, encendi´endola o apag´andola. Si la bombilla
#est´a encendida, se apagar´a y har´a mudar de estado a todas las bombillas de la misma
#fila y columna. Si la bombilla est´a apagada, se encender´a y de la misma manera
#har´a mudar de estado a todas las bombillas de la misma fila y columna.


from simpleai.search import astar, SearchProblem
from simpleai.search.viewers import WebViewer

initial = ((1, 0, 0), (1, 1, 0), (0, 1, 1))
goal = ((0, 0, 0), (0, 0, 0), (0, 0, 0))

def mudar(estado):
    if estado == 0:
        return 1
    else:
        return 0

def distinto(item, state):
    x, y = item
    stat = state[x]
    for i in stat:
        if i == 1:
            return True
    for i in state:
        if i[y] == 1:
            return True
    return False

class Bombillas(SearchProblem):
    def is_goal(self, state):
        return state == goal

    def cost(self, state1, action, state2):
        cont = 0
        for i in state2:
            for x in i:
                if x == 1:
                    cont += 1
        return cont

    def actions(self, state):
        acciones = []
        for anum, a in enumerate(state):
            for item, b in enumerate(a):
                acciones.append((anum, item))
        print 'ac', acciones
        return acciones

    def result(self, state, action):
        state = list((list(state[0]), list(state[1]), list(state[2])))
        lista, item = action
        for i in state[lista]:
            state[lista][i] = mudar(state[lista][i])
        for i, li in enumerate(state):
            state[i][item] = mudar(state[i][item])
        state = tuple((tuple(state[0]), tuple(state[1]), tuple(state[2])))
        return state

    def heuristic(self, state):
        cont = 0
        for i in state:
            for x in i:
                if x == 1:
                    cont += 1
        return cont

# Resolucion por A*
result = astar(Bombillas(initial))#, graph_search=True, viewer=WebViewer())
print 'result', result