#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#parsing file and creating graph

import re
import random

name = "exempleinstance.txt"
file = open(name, "r")

lines = file.readlines()

file.close()

NbSommet = int(lines[1])
graph = {}

for i in range(NbSommet):
    graph[int(lines[i+3])] = set()

NbArrete = int(lines[NbSommet + 4])

for i in range(NbArrete):
    x = re.split(" ", lines[i + NbSommet + 6])
    a = int(x[0])
    b = int(x[1])
    graph[a].add(b)
    graph[b].add(a)
    
#print(graph)

#2.1 delete a sommet

def deepCopy(graph):
    #create a copy of graph
    graph2 = {}
    for key in graph:
        graph2[key] = set()
        for val in graph[key]:
            graph2[key].add(val)
    return graph2

def deleteOne(graph, sommet):
    graph2 = deepCopy(graph)
    #delete an arrete
    for arrete in graph2[sommet]:
        graph2[arrete].remove(sommet)
    del graph2[sommet]
    return graph2

#2.2

def deleteSet(graph, mySet):
    graph2 = deepCopy(graph)
    for sommet in mySet:
        graph2 = deleteOne(graph2, sommet)
    return graph2

graph2 = deleteSet(graph, {1,2,3})
#print(graph2)

#2.3 degré des sommets

def degreSommets(graph):
    listeDegres = []
    for sommet in graph:
        listeDegres.append(len(graph[sommet]))
    return listeDegres

#print(degreSommets(graph))
#print(degreSommets(graph2))

#degré maximal
def degreMaximal(graph):
    liste = degreSommets(graph)
    maxDegre = max(liste)
    idMax = liste.index(maxDegre)
    return list(graph.keys())[idMax]

#Génération d'instances

def createGraph(n, p):
    newGraph = {}
    for i in range(n):
        newGraph[i] = set()
        
    for i in range(n):
        for j in range(i, n):
            r = random.random()
            if (r < p):
                newGraph[i].add(j)
                newGraph[j].add(i)
                
    return newGraph
        
generatedGraph = createGraph(5, 0.5)
print(generatedGraph)


# 3: Méthodes approchées

def algo_couplage(graph):
    C = set()
    for sommet in graph:
        if sommet not in C :
            for arrete in graph[sommet]:
                if arrete not in C :
                    C.add(sommet)
                    C.add(arrete)
    return C
            
def algo_glouton(graph):
    graph2 = deepCopy(graph)
    C = set()
    while sum(degreSommets(graph2))>0:
        v = degreMaximal(graph2)
        C.add(v)
        graph2 = deleteOne(graph2, v)
    return C

print("algo_couplage : ", algo_couplage(generatedGraph))

print("algo_glouton : ", algo_glouton(generatedGraph))