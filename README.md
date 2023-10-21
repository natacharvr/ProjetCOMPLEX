# Projet COMPLEX

### Natacha RIVIERE ET Imane HADBI

[Lien pour éditer ce markdown](https://hackmd.io/@e8Tyv4S8TlC0Zl1TAgWASg/SyrdJqFZT/edit)

## 2. Graphes

La représentation du graphe choisie est basée sur un dictionnaire Python. Dans cette représentation :

- Les clés du dictionnaire sont les sommets du graphe, qui sont généralement des entiers.
- Les valeurs associées à chaque clé sont des ensembles (sets) contenant les voisins de ce sommet.

## 3. Méthodes approchées

#### Question 1

Montrer que l'algorithme glouton n'est pas optimal :
Contrexemple :
Soit G=(V,E) un graphe

```mermaid
graph TD;
    A((A))
    B((B))
    C((C))
    D((D))
    E((E))
    F((F))
    G((G))
    A---B;
    A---D;
    A---F;
    B---C;
    D---E;
    F---G;
```
#### Déroulé de l'algorithme glouton :
##### Etape 1 : 
Sommet sélectionné : A
Nouveau graphe :
```mermaid
graph TD;
    B((B))
    C((C))
    D((D))
    E((E))
    F((F))
    G((G))
    B---C;
    D---E;
    F---G;
```
Les trois étapes suivantes sélectionneront un sommet pour chaque couple (B,C), (D,E) et (F,G).
Une couverture qui peut être obtenue est donc [A,B,D,F].

Or la solution optimale est [B,D,F]

Donc l'algorithme glouton n'est pas optimal. Le facteur d'approximation est $4\over3$. 
Par conséquent, dans ce cas, l'algorithme n'est pas $7\over6$-approchée.

### Question 2
#### Comparaison ( Glouton VS Couplage ):

##### Temps de calcul :
Le profil des deux courbes suivantes, avec des échelles logarithmiques, suggèrent que le temps d'éxécution des algorithmes couplages et glouton suivent une tendance exponentielle. Ce qui est cohérent avec le fait que le problème de couverture soit NP-complet, les algorithmes que nous utilisons ne sont pas polynomiaux.

En revanche, l'algorithme couplage est beaucoup plus rapide que l'algorithme glouton. En effet, pour une instance de 10 mille sommets, l'algorithme de couplage trouve une solution en environ 6 secondes, contre environ 35 secondes pour l'algorithme glouton.

On observe qu'en faisant varier p, le temps d'éxécution varie également. Plus p est grand, plus de temps de calcul est élevé, ce qui est cohérent car plus p est grand, plus l'algorithme doit traiter d'arêtes. En revanche, le profil des courbes reste exponentiel même avec p très petit.

![Couplage](plots/couplage_time.png)

![Glouton](plots/glouton_time.png)

##### Efficacité:
Les courbes suivantes ont pour objectif de déterminer quel algorithme est le plus efficace pour trouver une solution proche de l'optimal. On cherche à trouver une solution de taille minimale. On constate alors que l'algorithme glouton trouve toujours des meilleures solutions que l'algorithme de couplage. Cette différence est plus marquée sur des p plus petits. 
En revanche, elle est assez minime plus p augmente. A la lumière des analyses précédentes, on peut suggérer que même si l'algorithme glouton génère de meilleures solutions que l'algorithme de couplage, il est beaucoup trop lent à calculer et il vaudra mieux utiliser l'algorithme de couplage dans la suite de ce devoir.


![Efficacité](plots/efficacite_size.png)


## 4. Séparation et évaluation

#### Question 2

#### Algo Branchement basique:                
##### Temps d'exécution : 
L'algorithme de branchement basique parcours toutes les possibilités de couverture possible, ce qui revient à éxécuter $2^n$ fois l'algorithme de couplage. Quand n augmente, le nombre de calculs à effectuer augmente très vite. Avec cet algorithme, on peut trouver rapidement une solution pour un graphe de moins de 25 sommets. Au delà, les calculs sont trop longs.
Comme l'algorithme de couplage, qui est effectué pour chaque possibilité, est plus rapide pour des p plus petits, on retouve cette différence de vitesse dans les courbes suivantes.
##### Efficacité :
L'algo parvient à fournir la solution optimale. Cela signifie qu'il est capable de trouver la meilleure solution possible pour le problème donné. 

![Branchement](plots/branchementSimple.png)

### 4.2 Ajout de bornes
#### Question 1
Soit G un graphe, M un couplage, m le nombre d'arêtes de G de G et C une couverture de G. Alors :
$\lvert C \rvert \geq \max(b_1,b_2,b_3)$

avec :

$b_1 = \lceil{m\over\Delta}\rceil$ avec $\Delta$ le degré maximum des sommets du graphe

$b_2=\lvert{M}\rvert$

$b_3= {2n - 1 - \sqrt{(2n-1)^2 - 8m}\over 2}$

Montrons la validité des bornes :

##### Montrons $b_1$ :

Soit $G'=(S',E')$ ce graphe et $C'$ la couverture de ce graphe, de taille $x$.

Comme $C'$ est une couverture alors la somme des degrés de ses sommets est au moins égale à $m$.

$\sum_{i\in C'}{\lvert{i}\rvert} \geq m$

Comme le degré maximum des sommets est $\Delta$, on a 
$x \times \Delta \geq m$

$\Delta$ est positif et on travaille sur les entiers donc on a $x \geq \lceil{m\over \Delta}\rceil$

##### Montrons $b_2$ :
$b_2$ est valide car par définition, un couplage est un ensemble d'arêtes d'ayant pas d'extémité en commun. Il faut donc ajouter à la couverture au moins une des extrémités de chaque arête pour qu'elles soient toutes couvertes par notre couverture. 
Donc si on a un couplage M, on aura toujours au moins $\lvert{M}\rvert$ sommets dans une couverture.

##### Montrons $b_3$ :
TODO

#### Question 2 :
En ajoutant le calcul d'une borne inférieure et d'une borne supérieure en chaque noeud, on réduit énormément le nombre de calculs à faire car au lieu de calculer toutes les possibilités, on n'explore que les noeuds qui sont intéressants. 

Lorsque l'on compare les temps de calcul des deux algorithmes, la différence est très nette. L'algorithme borné prend beaucoup moins de temps que le précédent lorque n augmente.

![Comparaison1Branchement](plots/compareBranch1.png)


#### Question 3 :

#### Branchement amélioré 1: 
( prendre tous les voisins dans la 2eme branche )

##### Temps d'exécution : 
L'algorithme présente un temps d'exécution très faible, proche de zéro, pour la plupart des instances testées. Cela suggère une amélioration significative par rapport à l'algorithme de base, qui avait des temps d'exécution plus longs.

##### Efficacité : 
L'algorithme est toujours capable de produire des solutions optimales, dans un temps d'exécution très court.

![Branchement amelioré 1](plots/algo_ameliore1_tempsExec.png)

#### Branchement amélioré 2: 
( choisir le branchement de maniere à ce que le sommet soit de degre maximum )

##### Temps d'exécution : 
Les algorithmes "Amélioré 1" et "Amélioré 2" montrent des temps d'exécution extrêmement courts, presque nuls, dans la plupart des cas. Cependant, il est important de noter que "Amélioré 2" se distingue de manière significative par sa rapidité, surpassant généralement "Amélioré 1".

![Branchement amelioré1](plots/algo_ameliore2_tempsExec.png)

##### Efficacité : 
En ce qui concerne la qualité des solutions, les deux donnent des résultats similaires.

![Branchement amelioré1 VS 2](plots/efficacite_algo1_vs_algo2.png)

#### Question 4 :

Les algorithmes de couplage et glouton présentent généralement des rapports d'approximation élevés, proches de 1. Même lorsque la taille de l'instance "n" varie, les rapports d'approximation restent globalement performants, avec de légères fluctuations. Les pires rapports d'approximation observés étaient toujours proches de 1, confirmant la fiabilité de ces algorithmes pour résoudre le problème.

![rapport aprox](plots/rapportAprox.png)
