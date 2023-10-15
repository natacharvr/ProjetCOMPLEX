
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
    for sommet, aretes in graph.items():
        graph2[sommet] = set(aretes)
    return graph2



def deleteOne(graph, sommet):
    graph2 = {}
    for vertex, aretes in graph.items():
        if vertex != sommet:
            newAretes = set(aretes) - {sommet}
            graph2[vertex] = newAretes
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
        for j in range(i+1, n):
            r = random.random()
            if (r < p):
                newGraph[i].add(j)
                newGraph[j].add(i)
                
    return newGraph
        
generatedGraph = createGraph(5, 0.5)
#print(generatedGraph)


# 3: Méthodes approchées

def algo_couplage(graph):
    C = set()
    for sommet in graph:
        for arrete in graph[sommet]:
            if sommet not in C :
                if arrete not in C :
                    C.add(sommet)
                    C.add(arrete)
    return C
            
def algo_glouton(graph):

    graph2 = deepCopy(graph)
    C = set()
    somme = sum(degreSommets(graph2))
    while somme>0:      
        v = degreMaximal(graph2)
        C.add(v)
        #print(C)
        somme -= len(graph[v]) *2

        # deleteOne mais sans copie
        start = time.time()
        aretes_a_retirer = list(graph2[v])
        for arete in aretes_a_retirer:
            graph2[arete].remove(v)
        del graph2[v]
   
    return C


for i in range(1000, 10001, 1000) :
    for j in np.arange(0.2, 1, 0.2) :

        start = time.time()
        graphLu = lectureFichierPerso(str(i) + "_" + f'{j:.1f}')

        end = time.time()
        elapsed = end - start

        print(str(i) + "_" + f'{j:.1f}' + f'Temps d\'execution lecture : {elapsed:.5}ms')

        start = time.time()
        solCouplage = algo_couplage(graphLu)

        end = time.time()

        print("Taille instance couplage : " + str(len(solCouplage)))
        elapsed = end - start

        print(f'Temps d\'execution algo couplage : {elapsed:.5}s')

        start = time.time()
        solGlouton = algo_glouton(graphLu)
        end = time.time()

        print("Taille instance glouton : " + str(len(solGlouton)))
        elapsed = end - start

        print(f'Temps d\'execution algo glouton : {elapsed:.5}s')

# grapheTest = lectureFichierPerso("test")

# start = time.time()
# solCouplage = algo_glouton(grapheTest)

# end = time.time()

# print("Taille instance glouton : " + str(len(solCouplage)))
# elapsed = end - start

# print(f'Temps d\'execution algo glouton : {elapsed:.5}s')

#Section 4

#graph = {1:[2,3], 2:[1], 3:[1]}
# question 1
def branchement(graph):
    selectedArete = 0
    # On selectionne une arête 
    for sommet in graph.keys():
        if len(graph[sommet]) != 0:
            selectedArete = [sommet, min(graph[sommet])]
            break
    if selectedArete :
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec le sommet droit en moins
        g = etudierSommet(graph, selectedArete[0]) 
        d = etudierSommet(graph, selectedArete[1])

        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g[0] :
            return g
        else:
            return d
    else:
        # Il n'y a plus d'arêtes à étudier, la couveture es de taille 0
        return 0
    
def etudierSommet(graph, sommet):
    myGraph = deleteOne(graph, sommet) # On supprime le sommet donné
    selectedArete = 0
    # On selectionne une arête 
    for sommetEtudie in myGraph.keys():
        if len(myGraph[sommetEtudie]) != 0:
            selectedArete = [sommetEtudie, min(myGraph[sommetEtudie])]
            break
    if selectedArete :
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec le sommet droit en moins
        g = etudierSommet(myGraph, selectedArete[0])  
        d = etudierSommet(myGraph, selectedArete[1])
        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g :
            g[1].append(sommet)
            return [g[0] + 1, g[1]]
        else:
            d[1].append(sommet)
            return [d[0] + 1, d[1]]
    else:
        # Il n'y a plus d'arêtes à étudier, la couveture es de taille 1, le sommet retiré
        return [1, [sommet]]
    
# graph = {0: {1, 3, 4}, 1: {0, 2}, 2: {1}, 3: {0}, 4: {0}}
#print("solution : ", branchement(graph))

#question 2

def branchementCouplage(graph):
    selectedArete = 0
    #Calcul des bornes sup et inf
    borne_min = maxB(graph)
    borne_sup = algo_couplage(graph)
    # On selectionne une arête 
    for sommet in graph.keys():
        if len(graph[sommet]) != 0:
            selectedArete = [sommet, min(graph[sommet])]
            break
    if selectedArete :
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec le sommet droit en moins
        g = etudierSommetCouplage(graph, selectedArete[0], UB) 
        if (g[2]+1 <= UB) :
            UB = g[2] + 1
        d = etudierSommetCouplage(graph, selectedArete[1], UB)

        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g[0] :
            return g
        else:
            return d
    else:
        # Il n'y a pas d'arêtes à étudier, la couveture es de taille 0
        return 0
    
    
def etudierSommetCouplage(graph, sommet, UB):
    myGraph = deleteOne(graph, sommet) # On supprime le sommet donné
    selectedArete = 0
    #Calcul des bornes sup et bornes inf
    borne_min = maxB(myGraph)
    borne_sup = algo_couplage(myGraph)

    if (borne_min+1 >= UB) :
        return [math.inf, []] # La branche n'est pas intéressante
    
    if (borne_sup+1 <= UB) :
        UB = borne_sup+1 #On a trouvé une meilleure solution

    # On selectionne une arête 
    for sommetEtudie in myGraph.keys():
        if len(myGraph[sommetEtudie]) != 0:
            selectedArete = [sommetEtudie, min(myGraph[sommetEtudie])]
            break
    if selectedArete :
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec le sommet droit en moins
        g = etudierSommetCouplage(myGraph, selectedArete[0], UB-1)
        if (g[2]+1 <= UB) :
            UB = g[2] + 1
        d = etudierSommetCouplage(myGraph, selectedArete[1], UB-1)
        if (d[2]+1 <= UB) :
            UB = d[2] + 1
        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g :
            g[1].append(sommet)
            return [g[0] + 1, g[1], UB]
        else:
            d[1].append(sommet)
            return [d[0] + 1, d[1], UB]
    else:
        # Il n'y a plus d'arêtes à étudier, la couveture es de taille 1, le sommet retiré
        return [1, [sommet], UB]

def maxB(graph):
    graph2 = deepCopy(graph)
    couplage = algo_couplage(graph2)
    print("couplage : ", couplage)
    
    b2 = len(couplage)
    
    #décompte arêtes 
    delta = degreMaximal(graph2)
    m = 0
    for sommet in graph2:
        m+= len(graph2[sommet])
        for arrete in list(graph2[sommet]):
            graph2[arrete].remove(sommet)
        del graph2[sommet]

    b1 = math.ceil(m/delta)
    n = len(graph)
    b3 = ((2*n)-1-math.sqrt(((2*n-1)**2)-8*m))/2
    return max([b1, b2, b3])

# print("solution : ", branchementCouplage(graph))
