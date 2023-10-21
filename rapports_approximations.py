import matplotlib.pyplot as plt
import numpy as np
import re

def lectureFichier(name, size) :
    f = open(name, "r")
    lines = f.readlines()

    values_couplage = []
    values_glouton = []

    for a in range(0, size) :
        value_coupl = re.search("algo couplage : ([0-9]*)$", lines[a*4+1])
        value_glouton = re.search("algo glouton : ([0-9]*)$", lines[a*4+2])
        value_opt = re.search("solution ameliore 2:([0-9]*)$", lines[a*4+3])
        if (int(value_opt.group(1))) == 0 :
            values_couplage.append(1)
            values_glouton.append(1)
        else :
            values_couplage.append(int(value_coupl.group(1))/int(value_opt.group(1)))
            values_glouton.append(int(value_glouton.group(1))/int(value_opt.group(1)))

    return [values_couplage, values_glouton]
[values_couplage, values_glouton] = lectureFichier("benhmark\ValeursApproximation1.txt", 100)
max_couplage = 0
max_glouton = 0
for i in range(1,7):
    max_couplage = max(max(values_couplage), max_couplage)
    max_glouton = max(max(values_glouton), max_glouton)
    [values_couplage, values_glouton] = lectureFichier("benhmark\ValeursApproximation" + str(i) + ".txt", 100)

print("max_glouton", max_glouton)
print("max_couplage", max_couplage)
# for i in range(2, 7) :
#     [a,b] = lectureFichier("benhmark\ValeursApproximation" + str(i) + ".txt", 100)
#     for j in range(100) :
#         values_couplage[j] += a[j]
#         values_glouton[j] += b[j]
# for i in range(100) :
#     values_couplage[i] /= 7
#     values_glouton[i] /= 7

# fig, ax = plt.subplots()
# cmap = plt.get_cmap("winter", 4) 
# # plt.xlim(0.1,229)
# # plt.ylim(0, 1)
# ax.set_title("Comparaison des moyennes des rapports d'approximation \nde l'algorithme de couplage et glouton en fonction de n", pad=10)
# ax.plot([i for i in range(1,101, 4)], [values_couplage[j] for j in range(len(values_couplage)) if j%4==3], label="Couplage", color=cmap(2))
# ax.plot([i for i in range(1,101, 4)], [values_glouton[j] for j in range(len(values_glouton)) if j%4==3], label="Glouton", color=cmap(3))

# ax.legend()
# # ax.set_xscale('log')
# # ax.set_yscale('log')

# ax.set_xlabel("Taille de l'instance en sommets")
# ax.set_ylabel("Temps d'exécution (s)")
# plt.savefig('plots/rapports.png', dpi=300, bbox_inches='tight')
# plt.show()

