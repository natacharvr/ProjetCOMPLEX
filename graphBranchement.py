import matplotlib.pyplot as plt
import numpy as np
import re

def lectureFichier(name, size) :
    f = open(name, "r")
    lines = f.readlines()

    time_branchement = []

    for a in range(0, size) :
        branch_time = re.search("Temps d'execution algo naif : ([0-9]*.[0-9]*)s$", lines[a*2+1])
        time_branchement.append(float(branch_time.group(1)))
    return time_branchement

time_branchement = lectureFichier("benhmark/valeursBranchementsimple.txt", 96)

fig, ax = plt.subplots()
cmap = plt.get_cmap("bone", 6) 
plt.xlim(10,25)
# plt.ylim(0.1,50)
ax.set_title("Temps d'exécution moyen de l'algorithme \nde branchement simple en fonction de n", pad=10)
ax.plot([i for i in range(1,25)], [time_branchement[i] for i in range(len(time_branchement)) if i%4==3], '-o', label=f'$p={0.8}$', color=cmap(1))
ax.plot([i for i in range(1,25)], [time_branchement[i] for i in range(len(time_branchement)) if i%4==2], '-o', label=f'$p={0.6}$', color=cmap(2))
ax.plot([i for i in range(1,25)], [time_branchement[i] for i in range(len(time_branchement)) if i%4==1], '-o', label=f'$p={0.4}$', color=cmap(3))
ax.plot([i for i in range(1,25)], [time_branchement[i] for i in range(len(time_branchement)) if i%4==0], '-o', label=f'$p={0.2}$', color=cmap(4))
ax.legend()
# ax.set_xscale('log')
# ax.set_yscale('log')

ax.set_xlabel("Taille de l'instance en sommets")
ax.set_ylabel("Temps d'exécution (s)")
plt.savefig('plots/branchementSimple.png', dpi=300, bbox_inches='tight')
plt.show()

