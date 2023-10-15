
#parsing file and creating graph

import re
import random
import time
import math
import numpy as np

name = "exempleinstance.txt"
def lectureFichierStandard(name) :
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
    return graph
    
    #fonction définie pour étudier les fichiers générés par le code c
def lectureFichierPerso(name):
    file = open(name, "r")
    lines = file.readlines()

    file.close()

    NbSommet = int(lines[1])
    graph = {}

    for i in range(NbSommet):
        graph[int(lines[i+3])] = set()

    # Dans nos fichiers, le nombre d'arêtes est écrit en dernière ligne
    NbArrete = int(lines[-1])

    for i in range(NbArrete):
        x = re.split(" ", lines[i + NbSommet + 4])
        a = int(x[0])
        b = int(x[1])
        graph[a].add(b)
        graph[b].add(a)
    return graph
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

# graph2 = deleteSet(graph, {1,2,3})
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

#Génération d'instances (à éviter, plutôt utiliser le code c pour plus de rapidité)

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
#print(generatedGraph)


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

for i in range(10, 1000, 10) :
    for j in np.arange(0, 1, 0.2) :

        start = time.time()
        graphLu = lectureFichierPerso(str(i) + "_" + f'{j:.1f}')

        end = time.time()
        elapsed = end - start

        print(str(i) + "_" + f'{j:.1f}' + f'Temps d\'exécution lecture : {elapsed:.5}ms')

        start = time.time()
        solCouplage = algo_couplage(graphLu)
        # print("algo_couplage : ", )

        end = time.time()

        print("Taille instance couplage : " + str(len(solCouplage)))
        elapsed = end - start

        print(f'Temps d\'exécution algo couplage : {elapsed:.5}ms')

        start = time.time()
        solGlouton = algo_glouton(graphLu)
        end = time.time()

        print("Taille instance glouton : " + str(len(solGlouton)))
        elapsed = end - start

        print(f'Temps d\'exécution algo glouton : {elapsed:.5}ms')

#Section 4

#graph = {1:[2,3], 2:[1], 3:[1]}
# question 1
def branchement(graph):
    print(graph)
    selectedArete = 0
    for sommet in graph.keys():
        if len(graph[sommet]) != 0:
            selectedArete = [sommet, min(graph[sommet])]
            break
    if selectedArete :
        g = etudierSommet(graph, selectedArete[0]) 
        d = etudierSommet(graph, selectedArete[1])
        if min(g[0], d[0]) == g[0] :
            return g
        else:
            return d
    else:
        return 0
    
def etudierSommet(graph, sommet):
    myGraph = deleteOne(graph, sommet)
    selectedArete = 0
    for sommetEtudie in myGraph.keys():
        if len(myGraph[sommetEtudie]) != 0:
            selectedArete = [sommetEtudie, min(myGraph[sommetEtudie])]
            break
    if selectedArete :
        g = etudierSommet(myGraph, selectedArete[0])  
        d = etudierSommet(myGraph, selectedArete[1])
        if min(g[0], d[0]) == g :
            g[1].append(sommet)
            return [g[0] + 1, g[1]]
        else:
            d[1].append(sommet)
            return [d[0] + 1, d[1]]
    else:
        return [1, [sommet]]
    
# graph = {0: {1, 3, 4}, 1: {0, 2}, 2: {1}, 3: {0}, 4: {0}}
#print("solution : ", branchement(graph))

#question 2

def branchementCouplage(graph):
    print("graph : ", graph)
    selectedArete = 0
    maxB(graph)
    for sommet in graph.keys():
        if len(graph[sommet]) != 0:
            selectedArete = [sommet, min(graph[sommet])]
            break
    if selectedArete :
        g = etudierSommetCouplage(graph, selectedArete[0]) 
        d = etudierSommetCouplage(graph, selectedArete[1])
        if min(g[0], d[0]) == g[0] :
            return g
        else:
            return d
    else:
        return 0
    
    
def etudierSommetCouplage(graph, sommet):
    myGraph = deleteOne(graph, sommet)
    selectedArete = 0
    maxB(myGraph)
    for sommetEtudie in myGraph.keys():
        if len(myGraph[sommetEtudie]) != 0:
            selectedArete = [sommetEtudie, min(myGraph[sommetEtudie])]
            break
    if selectedArete :
        g = etudierSommetCouplage(myGraph, selectedArete[0])  
        d = etudierSommetCouplage(myGraph, selectedArete[1])
        if min(g[0], d[0]) == g :
            g[1].append(sommet)
            return [g[0] + 1, g[1]]
        else:
            d[1].append(sommet)
            return [d[0] + 1, d[1]]
    else:
        return [1, [sommet]]

def maxB(graph):
    graph2 = deepCopy(graph)
    couplage = algo_couplage(graph2)
    print("couplage : ", couplage)
    
    B2 = len(couplage)
    
    #décompte arêtes 
    delta = degreMaximal(graph2)
    m = 0
    for sommet in graph2:
        m+= len(graph2[sommet])
        for arrete in list(graph2[sommet]):
            graph2[arrete].remove(sommet)
        del graph2[sommet]

    b1 = math.ceil(m/delta)

# print("solution : ", branchementCouplage(graph))
