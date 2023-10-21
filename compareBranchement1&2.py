import matplotlib.pyplot as plt
import numpy as np
import re

def lectureFichier(name, size) :
    f = open(name, "r")
    lines = f.readlines()

    time_branchement = []
    time_branchement2 = []

    for a in range(0, size) :
        branch_time = re.search("Temps d'execution algo ameliore : ([0-9]*.[0-9]*)s$", lines[a*3+1])
        branch_time2 = re.search("Temps d'execution algo ameliore 2 : ([0-9]*.[0-9]*)s$", lines[a*3+2])

        time_branchement.append(float(branch_time.group(1)))
        time_branchement2.append(float(branch_time2.group(1)))

    return [time_branchement, time_branchement2]

[time_branchement, time_branchement2] = lectureFichier("benhmark/ComparaisonBranchementsAmeliorés08.txt", 99)

fig, ax = plt.subplots()
cmap = plt.get_cmap("copper", 4) 
# plt.xlim(0.1,229)
# plt.ylim(0.1,50)
ax.set_title("Comparaison des temps d'exécution des algorithmes de\n branchements améliorés 1 et 2 pour p=0.8", pad=10)
ax.plot([i for i in range(1,100)], time_branchement, label="Version 1", color=cmap(1))
ax.plot([i for i in range(1,100)], time_branchement2, label="Version 2", color=cmap(2))
# ax.plot([i for i in range(1,85)], [time_branchement[i] for i in range(len(time_branchement)) if i%4==2], label=f'$p={0.6}$', color=cmap(2))
# ax.plot([i for i in range(1,85)], [time_branchement[i] for i in range(len(time_branchement)) if i%4==3], label=f'$p={0.8}$', color=cmap(1))

ax.legend()
# ax.set_xscale('log')
# ax.set_yscale('log')

ax.set_xlabel("Taille de l'instance en sommets, échelle logarithmique")
ax.set_ylabel("Temps d'exécution (s), échelle logarithmique")
plt.savefig('plots/compareAmeliorés08.png', dpi=300, bbox_inches='tight')
plt.show()

