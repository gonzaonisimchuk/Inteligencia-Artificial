# coding: utf-8
#En una mesa se encuentran dos jarras, una con capacidad para 3 litros (llamada Tres,
#y la otra con capacidad para 4 litros (llamada Cuatro). Inicialmente, Tres y Cuatro
#est´an vac´ıas. Cualquiera de ellas puede llenarse con el agua de un grifo G. Asimismo,
#el contenido de las jarras se puede vaciar en una pila P. Tambi´en es posible verter el
#agua de una jarra en la otra. No se dipone de dispositivos de medici´on adicionales.
#Se trata de encontrar una secuencia de operadores que deje exactamente dos litros
#de agua en Cuatro.
#(a) Modela este problema como un problema de b´usqueda. Tendr´as que definir, por
#tanto, un estado inicial, el conjunto de estados meta, los operadores (especificando
#sus precondiciones y postcondiciones), as´ı como el coste de cada operador.
#(b) Caracteriza el conocimiento a priori del agente de resoluci´on del problema correspondiente.
#(c) Encuentra una soluci´on al problema utilizando un algoritmo de b´usqueda en
#amplitud.

from simpleai.search import astar, SearchProblem
from simpleai.search.viewers import WebViewer, ConsoleViewer

initial = (0, 0) # jarra 3 , jarra 4

def cat_pasar(state, jarra):
    tres, cuatro = state
    dtres = 3 - tres
    dcuatro = 4 - cuatro
    if jarra == 0 and dcuatro == 0:
        return 0
    elif jarra == 1 and dtres == 0:
        return 0
    if jarra == 0:
        if dcuatro > tres:
            return tres
        else:
            return dcuatro
    elif jarra == 1:
        if dtres > cuatro:
            return cuatro
        else:
            return dtres


class Jarra(SearchProblem):
    def is_goal(self, state):
        return state[1] == 2

    def cost(self, state1, action, state2):
        return action[1] + 3

    def actions(self, state):
        acciones = []
        for enum, s in enumerate(state):
            if s == 0:
                acciones.append(('A', enum))
            else:
                acciones.append(('V', enum))
            if s != 0 and cat_pasar(state, enum) > 0:
                acciones.append(('C', enum))
        return acciones

    def result(self, state, action):
        accion, s = action
        state = list(state)
        if accion == 'A':
            state[s] = 3 + s
        elif accion == 'V':
            state[s] = 0
        elif accion == 'C':
            cant = cat_pasar(state, s)
            if s == 0:
                state[0] -= cant
                state[1] += cant
            elif s == 1:
                state[0] += cant
                state[1] -= cant
        return tuple(state)

    def heuristic(self, state):
        return abs(state[1] - 2)

# Resolucion por A*
result = astar(Jarra(initial), graph_search=True, viewer=WebViewer())
print 'result', result
print 'path', result.path()