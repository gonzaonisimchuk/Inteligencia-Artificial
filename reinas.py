# -*- coding: utf-8 -*-
 #El problema de las 4 reinas consiste en colocar 4 reinas en un tablero de ajedrez 4x4
#de modo que ninguna sea amenazada por otra reina
#(a) Modelizar el problema como CSP, identificando el conjunto de variables, el dominio
#de cada variable y el conjuntos de restricciones binaria.
#(b) Aplique el algoritmo MAC para resolver el problema. Las heur´ısticas a usar son
#las siguientes: las filas se eligen consecutivamente (esto es, primero x1, luego x2,
#etc.), y para asignar una columna se debe elegir el valor m´as peque˜no

import itertools
from simpleai.search import CspProblem, backtrack, MOST_CONSTRAINED_VARIABLE, LEAST_CONSTRAINING_VALUE, HIGHEST_DEGREE_VARIABLE, min_conflicts

variables = range(1, 5)
dominios = {}

for var in variables:
    dominios[var] = range(1, 5)

orden = []

def fila(variables, dominios):
    return dominios[0] != dominios[1]

def diagonal(variables, dominios):
    fila_a = dominios[0]
    columna_a = variables[0]
    fila_b = dominios[1]
    columna_b = variables[1]
    return abs(fila_a - fila_b) != abs(columna_a - columna_b)


for par in itertools.combinations(variables, 2):
    orden.append((par, fila))
    orden.append((par, diagonal))

problem = CspProblem(variables, dominios, orden)

result = backtrack(problem,
           variable_heuristic=MOST_CONSTRAINED_VARIABLE,
           value_heuristic=LEAST_CONSTRAINING_VALUE,
           inference=True)

print result