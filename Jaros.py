from simpleai.search import SearchProblem, astar
from simpleai.search.viewers import WebViewer, ConsoleViewer

n = 4 #cantidadjaros
initial = []
for i in range(1, n):
    initial.append(0)
initial.append(n)
initial = tuple(initial)

def pasarCap(jarroO, litrosO):
    return (jarroO + 1) - litrosO

class Jarros(SearchProblem):
    def cost(self, state1, action, state2):
        return action[0] + 1

    def is_goal(self, state):
        for stat in state:
            if stat == 0:
                return False
        return True

    def actions(self, state):
        acciones = []
        for jarroO, litrosO in enumerate(state):
            for jarroD, litrosD in enumerate(state):
                #print 'jarroO', jarroO, litrosO
                #print 'JarroD', jarroD, litrosD
                if litrosD > 0 and pasarCap(jarroO, litrosO) > 0:
                    acciones.append((jarroO, jarroD))
        return acciones

    def result(self, state, action):
        jarroO, jarroD = action
        litrosO, litrosD = state[jarroO], state[jarroD]
        pasar = pasarCap(jarroO, litrosO)
        minPasar = min(litrosD, pasar)
        state = list(state)
        state[jarroO] += minPasar
        state[jarroD] -= minPasar
        return tuple(state)

    def heuristic(self, state):
        cont = 0
        for i in state:
            if i == 0:
                cont += 1
        return cont

result = astar(Jarros(initial), graph_search=True, viewer=WebViewer())

print 'result: ', result