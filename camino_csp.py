# -*- coding: utf-8 -*-

#http://www.ia.urjc.es/cms/IA4

#Un representante comercial tiene que visitar 6 clientes (Repsol, Telef´onica, ACS,
#Endesa, Iberdrola, Uni´on Fenosa) en un d´ıa laborable (de 9 a 19). No se puede visitar
#dos clientes en la misma hora. Adem´as hay que visitar los clientes ACS y Uni´on
#Fenosa antes de Endesa. Repsol est´a fuera de Madrid, mientras que todos los dem´as
#est´an en Plaza de Castilla. Por lo tanto, para ir de Repsol a cualquier otro cliente se
#tarda dos horas, mientras que para ir de un cliente a otro en Plaza de Castilla no se
#tarda nada. Florentino P´erez de ACS solo puede recibir el representante de 15 a 17
#(luego se va al Bernabeu a ver la Champions).
#(a) Modelizar el problema como CSP, identificando el conjunto de variables, el dominio
#de cada variable y el conjuntos de restricciones. Dibuje el grafo de restricciones.
#(b) Aplique el algoritmo de b´usqueda con backtracking para encontrar una soluci´on.
#Evaluar las variables y los valores a asignar en el orden dado (es decir Repsol,
#Telef´onica, ... Uni´on Fenosa, y 9, 10, 11, ..., 19)

import itertools
from simpleai.search import CspProblem, backtrack, MOST_CONSTRAINED_VARIABLE, LEAST_CONSTRAINING_VALUE, HIGHEST_DEGREE_VARIABLE, min_conflicts

variables = ('R', 'T', 'A', 'E', 'I', 'U')
dominios = {}
clientes = list(range(9, 19))

for var in variables:
    if var == 'U':
        dominios[var] = [9]
    else:
        dominios[var] = clientes

def distintos(variables, dominios):
    return dominios[0] != dominios[1]

def antes(variables, dominios):
    #if variables[0] == 'A' and (variables[1] == 'E' or variables[1] == 'R'):
    return dominios[0] < dominios[1]

orden = []

for par in itertools.combinations(variables, 2):
    orden.append((par, distintos))
    if (variables[0] == 'A' and variables[1] == 'E'):
        orden.append((par, antes))
    if (variables[0] == 'A' and variables[1] == 'R'):
        orden.append((par, antes))
    if (variables[0] == 'U' and variables[1] == 'E'):
        orden.append((par, antes))
    if (variables[0] == 'U' and variables[1] == 'R'):
        orden.append((par, antes))

problem = CspProblem(variables, dominios, orden)

result = backtrack(problem,
           variable_heuristic=MOST_CONSTRAINED_VARIABLE,
           value_heuristic=LEAST_CONSTRAINING_VALUE,
           inference=True)

print result