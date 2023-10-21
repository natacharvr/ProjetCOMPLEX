import matplotlib.pyplot as plt
import numpy as np
import re

def lectureFichier(name, size) :
    f = open(name, "r")
    lines = f.readlines()

    time_branchement = []

    for a in range(0, size) :
        branch_time = re.search("Temps d'execution algo ameliore : ([0-9]*.[0-9]*)s$", lines[a*2+1])
        time_branchement.append(float(branch_time.group(1)))
    return time_branchement

time_branchement= lectureFichier("benhmark/ValeursBranchementAmeliore.txt", 228)

fig, ax = plt.subplots()
cmap = plt.get_cmap("RdPu", 3) 
# plt.xlim(0.1,229)
# plt.ylim(0.1,50)
ax.set_title("Temps d'éxécution de l'algorithme de branchement amélioré 1\n en fonction de la taille des instances", pad=10)
ax.plot([i for i in range(22,229)], time_branchement[21:], label=f'$p={0.8}$', color=cmap(1))

ax.legend()
ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xlabel("Taille de l'instance en sommets, échelle logarithmique")
ax.set_ylabel("Temps d'exécution (s), échelle logarithmique")
plt.savefig('plots/branchAmeliore1.png', dpi=300, bbox_inches='tight')
plt.show()

