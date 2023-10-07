
#parsing file and creating graph

import re
import random
import time

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
    for arrete in list(graph2[sommet]):
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
        
generatedGraph = createGraph(100, 0.5)
print(generatedGraph)


# 3: Méthodes approchées

def algo_couplage(graph):
    C = []
    for sommet in graph:
        if sommet not in C :
            for arrete in graph[sommet]:
                if arrete not in C :
                    C.append(sommet)
                    C.append(arrete)
                    #print(C)
    return C
            
def algo_glouton(graph):
    graph2 = deepCopy(graph)
    C = []
    while sum(degreSommets(graph2))>0:
        v = degreMaximal(graph2)
        C.append(v)
        #print(C)
        graph2 = deleteOne(graph2, v)
    return C

start = time.time()

print("algo_couplage : ", algo_couplage(generatedGraph))

end = time.time()
elapsed = end - start

print(f'Temps d\'exécution algo couplage : {elapsed:.2}ms')

start = time.time()

print("algo_glouton : ", algo_glouton(generatedGraph))

end = time.time()
elapsed = end - start

print(f'Temps d\'exécution algo glouton : {elapsed:.2}ms')