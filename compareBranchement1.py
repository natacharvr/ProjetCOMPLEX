import matplotlib.pyplot as plt
import numpy as np
import re

def lectureFichier(name, size) :
    f = open(name, "r")
    lines = f.readlines()

    time_branchement = []
    time_branchement2 = []

    for a in range(0, size) :
        branch_time = re.search("Temps d'execution algo naif : ([0-9]*.[0-9]*)s$", lines[a*3+1])
        branch2_time = re.search("Temps d'execution algo pas naif : ([0-9]*.[0-9]*)s$", lines[a*3+2])
        time_branchement.append(float(branch_time.group(1)))
        time_branchement2.append(float(branch2_time.group(1)))
    return [time_branchement, time_branchement2]

[time_branchement, time_branchement2] = lectureFichier("benhmark/valeursComparéeBranchement1.txt", 25)

fig, ax = plt.subplots()
cmap = plt.get_cmap("Greens", 3) 
plt.xlim(10,26)
# plt.ylim(0.1,50)
ax.set_title("Comparaison des temps d'éxécution des algorithmes\n de branchement simple et bornée", pad=10)
ax.plot([i for i in range(1,26)], [time_branchement[i] for i in range(len(time_branchement))], '-o', label="branchement simple", color=cmap(2))
ax.plot([i for i in range(1,26)], [time_branchement2[i] for i in range(len(time_branchement2))], '-o', label="version bornée", color=cmap(1))

ax.legend()
# ax.set_xscale('log')
# ax.set_yscale('log')

ax.set_xlabel("Taille de l'instance en sommets")
ax.set_ylabel("Temps d'exécution (s)")
plt.savefig('plots/compareBranch1.png', dpi=300, bbox_inches='tight')
plt.show()

