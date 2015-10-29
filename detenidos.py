# -*- coding: utf-8 -*-

#1. La policia ha detenido a 5 sospechosos, A, B, C, D, E.
#Hay 5 testigos, y cada uno hace hace dos declaraciones: una es cierta y la otra es
#falsa.
#Testigo 1: 2 es A — 3 es B
#Testigo 2: 1 es C — 2 es D
#Testigo 3: 3 es D — 5 es C
#Testigo 4: 2 es A — 4 es E
#Testigo 5: 4 es E — 1 es B
#(a) Identificar los sospechosos 1,2,3,4 y 5 en base a las declaraciones de los testigos,
#formulando el problema como CSP y aplicando chronological backtracking con
#forward checking (es decir, cada vez que se asigna un valor a una variable,
#compruebo los dominios de los “vecinos” de dicha variable).

import itertools
from simpleai.search import CspProblem, backtrack, MOST_CONSTRAINED_VARIABLE, LEAST_CONSTRAINING_VALUE, HIGHEST_DEGREE_VARIABLE, min_conflicts

testigos = (((2, 'A'), (3, 'B')),
            ((1, 'C'), (2, 'D')),
            ((3, 'D'), (5, 'C')),
            ((2, 'A'), (4, 'E')),
            ((5, 'E'), (1, 'B')))

variables = range(1,6)
dom = ['A', 'B', 'C', 'D', 'E']
dominios = {}

for var in variables:
    vdom = []
    for testigo in testigos:
        for cc in testigo:
            if cc[0] == var and vdom.count(cc[1]) == 0:
                vdom.append(cc[1])
    dominios[var] = vdom

orden = []

def valid(variables, dominios):
    return dominios[0] != dominios[1]

for par in itertools.combinations(variables, 2):
    orden.append((par, valid))

problem = CspProblem(variables, dominios, orden)

##if metodo_busqueda == 'backtrack':
result = backtrack(problem,
           variable_heuristic=MOST_CONSTRAINED_VARIABLE,
           value_heuristic=LEAST_CONSTRAINING_VALUE,
           inference=True)
    #if metodo_busqueda == 'min_conflicts':
        ##result = min_conflicts(problem, initial_assignment=None, iterations_limit=1000)

print result
#