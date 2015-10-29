# -*- coding: utf-8 -*-
from simpleai.search import SearchProblem, hill_climbing, beam, hill_climbing_random_restarts
from simpleai.search.viewers import ConsoleViewer, WebViewer, BaseViewer
from random import randint

GOAL = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

INITIAL = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1),
)

def find(state, num):
    for enum, item in enumerate(state):
        for en, it in enumerate(item):
            if it == num:
                return (enum, en)
    return None

class Puzzle(SearchProblem):
    def actions(self, state):
        acciones = []
        enum, en = find(state, 0)
        if enum > 0:
            acciones.append((1, 0))
        if en > 0:
            acciones.append((0, -1))
        if enum < 2:
            acciones.append((-1, 0))
        if en < 2:
            acciones.append((0, +1))
        return acciones

    def result(self, state, action):
        state = list((list(state[0]), list(state[1]), list(state[2])))
        aenum, aen = find(state, 0)
        enum, en = aenum + action[0], aen + action[0]
        val = state[enum][en]
        print 'state', state, 'ac', action
        if val == 0:
            return 'a' + 1
        state[aenum][aen] = val
        state[enum][en] = 0
        return tuple(state)

    def value(self, state):
        cant = 0
        for enum, item in enumerate(state):
            for en, it in enumerate(item):
                if it != GOAL[enum][en]:
                    cant += it
        return -cant

    def generate_random_state(self):
        initial = list((list(INITIAL[0]), list(INITIAL[1]), list(INITIAL[2])))
        enum, en = find(initial, 0)
        aenum, aen = find(initial, randint(1, 8))
        initial[enum][en] = initial[aenum][aen]
        initial[aenum][aen] = 0
        return tuple((tuple(initial[0]), tuple(initial[1]), tuple(initial[2])))

visor = BaseViewer()
reinicios = 1000
resultado = hill_climbing_random_restarts(Puzzle(INITIAL), iterations_limit=1000, restarts_limit=reinicios, viewer=visor)
#resultado = hill_climbing_random_restars(Puzzle(INITIAL), viewer=visor)
print 'path', resultado.path()
print 'resultado', resultado
print 'visor', visor.stats