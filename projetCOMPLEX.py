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
    M=0
    for sommet in graph:
        for arrete in graph[sommet]:
            if sommet not in C :
                if arrete not in C :
                    C.add(sommet)
                    C.add(arrete)
                    M+=1
    return [C, M]
            
def algo_glouton(graph):
    graph2 = deepCopy(graph)
    C = set()
    somme = sum(degreSommets(graph2))
    while somme>0:      
        v = degreMaximal(graph2)
        C.add(v)
        somme -= len(graph2[v]) *2

        # deleteOne mais sans copie
        
        aretes_a_retirer = list(graph2[v])
        for arete in aretes_a_retirer:
            graph2[arete].remove(v)
        del graph2[v]

    return C

# name = "values5.txt"
# f = open(name, "w")
# for i in range(1000, 5001, 1000) :
#     for j in np.arange(0.05, 0.19, 0.05) :

#        start = time.time()
#        graphLu = lectureFichierPerso(str(i) + "_" + f'{j:.2f}')

#        end = time.time()
#        elapsed = end - start

#        f.write(str(i) + "_" + f'{j:.2f}'+"\n")

#        start = time.time()
#        solCouplage = algo_couplage(graphLu)

#        end = time.time()

#        f.write("Taille instance couplage : " + str(len(solCouplage[0]))+'\n')
#        elapsed = end - start

#        f.write(f'Temps d\'execution algo couplage : {elapsed:.5}s'+"\n")

#        start = time.time()
#        solGlouton = algo_glouton(graphLu)
#        end = time.time()

#        f.write("Taille instance glouton : " + str(len(solGlouton))+"\n")
#        elapsed = end - start

#        f.write(f'Temps d\'execution algo glouton : {elapsed:.5}s'+ "\n")
# f.close()

# grapheTest = createGraph(5000, 0.6)

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
        return [0, []]
    
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
        if min(g[0], d[0]) == g[0] :
            g[1].append(sommet)
            return [g[0] + 1, g[1]]
        else:
            d[1].append(sommet)
            return [d[0] + 1, d[1]]
    else:
        # Il n'y a plus d'arêtes à étudier, la couveture es de taille 1, le sommet retiré
        return [1, [sommet]]
    
# graph = {0: {1, 3, 4}, 1: {0, 2}, 2: {1}, 3: {0}, 4: {0}}
# print("solution : ", branchement(graph))

#question 2

UB = math.inf

def branchementCouplage(graph):
    selectedArete = 0
    
    # On selectionne une arête 
    for sommet in graph.keys():
        if len(graph[sommet]) != 0:
            selectedArete = [sommet, min(graph[sommet])]
            break
    if selectedArete :
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec le sommet droit en moins
        g = etudierSommetCouplage(graph, selectedArete[0], 1) 
        d = etudierSommetCouplage(graph, selectedArete[1], 1)
        # print("g: ", g, "d: ", d)
        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g[0] :
            return g
        else:
            return d
    else:
        # Il n'y a pas d'arêtes à étudier, la couveture es de taille 0
        return [0, []]

    
def etudierSommetCouplage(graph, sommet, profondeur):
    myGraph = deleteOne(graph, sommet) # On supprime le sommet donné
    selectedArete = 0
    # On selectionne une arête 
    for sommetEtudie in myGraph.keys():
        if len(myGraph[sommetEtudie]) != 0:
            selectedArete = [sommetEtudie, min(myGraph[sommetEtudie])]
            break
    if selectedArete :
        #Calcul des bornes sup et bornes inf
        couplage = algo_couplage(myGraph)
        borne_min = maxB(myGraph, couplage)
        global UB
        if (borne_min+profondeur > UB) : 
            return [math.inf, []] # La branche n'est pas intéressante
        
        borne_sup = len(couplage[0])

        if (borne_sup+profondeur <= UB) :
            UB = borne_sup+profondeur #On a trouvé une meilleure solution
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec le sommet droit en moins
        g = etudierSommetCouplage(myGraph, selectedArete[0], profondeur+1)
        d = etudierSommetCouplage(myGraph, selectedArete[1], profondeur+1)


        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g[0] :
            g[1].append(sommet)
            return [g[0] + 1, g[1]]
        else:
            d[1].append(sommet)

            return [d[0] + 1, d[1]]
    else:
        # Il n'y a plus d'arêtes à étudier, la couveture es de taille 1, le sommet retiré
        return [1, [sommet]]

def maxB(graph, couplage):
    graph2 = deepCopy(graph)    
    b2 = couplage[1]
    
    #décompte arêtes 
    deg = degreSommets(graph2)
    delta = max(deg)
    m = sum(deg) / 2
    b1 = math.ceil(m/delta)

    n = len(graph)
    b3 = ((2*n)-1-math.sqrt(((2*n-1)**2)-8*m))/2
    return max([b1, b2, b3])


# graph = {0: {2}, 1: {3, 4}, 2: {0}, 3: {1, 4}, 4: {1, 3}}
# graph = createGraph(28, 0.5)
# start = time.time()
# a = branchementCouplage(graph)
# end = time.time()

# elapsed = end - start

# print(f'Temps d\'execution algo pas naif : {elapsed:.5}s')
# print("solution pas naive :", a)

# start = time.time()
# a = branchement(graph)
# end = time.time()

# elapsed = end - start

# print(f'Temps d\'execution algo naif : {elapsed:.5}s')
# print("solution naive :", a)


# section 4.3

UB_ameliore = math.inf

def branchementCouplageAmeliore(graph):
    selectedArete = 0
    
    # On selectionne une arête 
    for sommet in graph.keys():
        if len(graph[sommet]) != 0:
            selectedArete = [sommet, min(graph[sommet])]
            break
    if selectedArete :
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec le sommet droit en moins
        g = etudierSommetCouplageAmeliore(graph, [selectedArete[0]], 1) 

        d = etudierSommetCouplageAmeliore(graph, list(graph[selectedArete[0]]), len(graph[selectedArete[0]])) #on passe une liste de toujs les sommets reliés à u
        # print("g: ", g, "d: ", d)
        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g[0] :
            return g
        else:
            return d
    else:
        # Il n'y a pas d'arêtes à étudier, la couveture est de taille 0
        return [0, []]

    
def etudierSommetCouplageAmeliore(graph, sommets, profondeur):
    myGraph = deleteSet(graph, sommets) # On supprime le sommet donné
    selectedArete = 0
    # On selectionne une arête 
    for sommetEtudie in myGraph.keys():
        if len(myGraph[sommetEtudie]) != 0:
            selectedArete = [sommetEtudie, min(myGraph[sommetEtudie])]
            break
    if selectedArete :
        #Calcul des bornes sup et bornes inf
        couplage = algo_couplage(myGraph)
        borne_min = maxB(myGraph, couplage)
        global UB_ameliore
        if (borne_min+profondeur > UB_ameliore) : 
            return [math.inf, []] # La branche n'est pas intéressante
        
        borne_sup = len(couplage[0])

        if (borne_sup+profondeur <= UB_ameliore) :
            UB_ameliore = borne_sup+profondeur #On a trouvé une meilleure solution
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec tous ses voisins
        g = etudierSommetCouplageAmeliore(myGraph, [selectedArete[0]], profondeur+1)
        d = etudierSommetCouplageAmeliore(myGraph, list(myGraph[selectedArete[0]]), profondeur+len(myGraph[selectedArete[0]]))


        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g[0] :
            return [g[0] + len(sommets), g[1] + sommets]
        else:
            return [d[0] + len(sommets), d[1]+ sommets]
    else:
        # Il n'y a plus d'arêtes à étudier, la couveture es de taille 1, le sommet retiré
        return [len(sommets), sommets]
    
# graph = createGraph(100, 0.1)
# print(graph)
# print("version améliorée : ",branchementCouplageAmeliore(graph))
# print("version de base ",branchementCouplage(graph))

# graph = createGraph(28, 0.5)
# start = time.time()
# # a = branchementCouplage(graph)
# end = time.time()

# elapsed = end - start

# print(f'Temps d\'execution algo pas naif : {elapsed:.5}s')
# # print("solution pas naive :", a)

# start = time.time()
# a = branchementCouplageAmeliore(graph)
# end = time.time()

# elapsed = end - start

# print(f'Temps d\'execution algo ameliore : {elapsed:.5}s')
# print("solution :", a)

# 4.3 question 2

UB_ameliore2 = math.inf

def branchementCouplageAmeliore2(graph):
    # selectedArete = 0
    
    # On selectionne le sommet maximal
    u = degreMaximal(graph)
    
    if len(graph[u]) > 0 :
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec le sommet droit en moins
        g = etudierSommetCouplageAmeliore2(graph, [u], 1) 

        d = etudierSommetCouplageAmeliore2(graph, list(graph[u]), len(graph[u])) #on passe une liste de toujs les sommets reliés à u
        # print("g: ", g, "d: ", d)
        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g[0] :
            return g
        else:
            return d
    else:
        # Il n'y a pas d'arêtes à étudier, la couveture es de taille 0
        return [0, []]

    
def etudierSommetCouplageAmeliore2(graph, sommets, profondeur):
    myGraph = deleteSet(graph, sommets) # On supprime le sommet donné
    
    u = degreMaximal(myGraph)
    if len(myGraph[u]) > 0 :
        #Calcul des bornes sup et bornes inf
        couplage = algo_couplage(myGraph)
        borne_min = maxB(myGraph, couplage)
        global UB_ameliore2
        if (borne_min+profondeur > UB_ameliore2) : 
            return [math.inf, []] # La branche n'est pas intéressante
        
        borne_sup = len(couplage[0])

        if (borne_sup+profondeur <= UB_ameliore2) :
            UB_ameliore2 = borne_sup+profondeur #On a trouvé une meilleure solution
        #Il y a des arêtes, on crée un noeud avec le sommet gauche en moins et un autre avec tous ses voisins
        g = etudierSommetCouplageAmeliore2(myGraph, [u], profondeur+1)
        d = etudierSommetCouplageAmeliore2(myGraph, list(myGraph[u]), profondeur+len(myGraph[u]))


        #Si la solution de gauche est la meilleure, on la renvoie, l'autre sinon
        if min(g[0], d[0]) == g[0] :
            return [g[0] + len(sommets), g[1] + sommets]
        else:
            return [d[0] + len(sommets), d[1]+ sommets]
    else:
        # Il n'y a plus d'arêtes à étudier, la couveture es de taille 1, le sommet retiré
        return [len(sommets), sommets]
    

f = open("benhmark/valeursBranchementsimple.txt", "w")
for i in range(1, 26) :
    print(i)
    for p in np.arange(0.2, 0.8, 0.2) :
        f.write(str(i) + "_" + str(p) + "\n")
        graph = createGraph(i, p)

        # start = time.time()
        # a = branchementCouplageAmeliore(graph)
        # end = time.time()
        # elapsed = end - start
        # print(f'Temps d\'execution algo ameliore : {elapsed:.5}s')
        # print("solution algo ameliore:", a[0])

        # start = time.time()
        # a = branchementCouplageAmeliore2(graph)
        # end = time.time()
        # elapsed = end - start
        # print(f'Temps d\'execution algo ameliore 2 : {elapsed:.5}s')
        # print("solution ameliore 2:", a[0])

        start = time.time()
        a = branchement(graph)
        end = time.time()
        elapsed = end - start
        f.write(f'Temps d\'execution algo naif : {elapsed:.5}s' + '\n')
        # f.write("solution naive :" + str(a[0]) + '\n')

        # start = time.time()
        # a = branchementCouplage(graph)
        # end = time.time()
        # elapsed = end - start
        # f.write(f'Temps d\'execution algo pas naif : {elapsed:.15}s' + '\n')
        # f.write("solution pas naive :", a[0])

        # print("\n\n\n")

    UB = math.inf
#         UB_ameliore = math.inf
#         UB_ameliore2 = math.inf