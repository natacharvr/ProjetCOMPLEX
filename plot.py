import matplotlib.pyplot as plt
import numpy as np
import re

plt.rc('font', size='13')

def lectureFichier(name, size) :
    f = open(name, "r")
    lines = f.readlines()

    time_couplage = []
    time_glouton = []
    size_couplage = []
    size_glouton = []

    for a in range(0, size) :
        coupl_size = re.search("Taille instance couplage : ([0-9]*)", lines[a*5+1])
        size_couplage.append(int(coupl_size.group(1)))

        coupl_time = re.search("Temps d'execution algo couplage : ([0-9]*.[0-9]*)s$", lines[a*5+2])
        time_couplage.append(float(coupl_time.group(1)))

        glout_size = re.search("Taille instance glouton : ([0-9]*)", lines[a*5+3])
        size_glouton.append(int(glout_size.group(1)))

        glout_time = re.search("Temps d'execution algo glouton : ([0-9]*.[0-9]*)s$", lines[a*5+4])
        time_glouton.append(float(glout_time.group(1)))
    return [time_couplage, time_glouton, size_couplage, size_glouton]

[time_couplage, time_glouton, size_couplage, size_glouton] = lectureFichier("benhmark/values1.txt", 30)

for i in range(2, 11) :
    name = "benhmark/values" + str(i) + ".txt"
    [time_couplage2, time_glouton2, size_couplage2, size_glouton2] = lectureFichier(name, 30)
    for j in range (0, 30) :
        time_couplage[j] = (time_couplage[j] + time_couplage2[j])
        time_glouton[j] = (time_glouton[j] + time_glouton2[j])
        size_couplage[j] = (size_couplage[j] + size_couplage2[j])
        size_glouton[j] = (size_glouton[j] + size_glouton2[j])

for j in range (0, 30) :
    time_couplage[j] = time_couplage[j]/10
    time_glouton[j] = time_glouton[j]/10
    size_couplage[j] = size_couplage[j]/10
    size_glouton[j] = size_glouton[j]/10


fig, ax = plt.subplots()
cmap = plt.get_cmap("Blues", 4) 
plt.xlim(0,11000)
plt.ylim(0,7)
ax.set_title("Temps d'exécution moyen de l'algorithme \nde couplage en fonction de n", pad=10)
ax.plot([i for i in range(1000,10001, 1000) if True], [time_couplage[i] for i in range(len(time_couplage)) if i%3==0], '-o', label=f'$p={0.2}$', color=cmap(1))
ax.plot([i for i in range(1000,10001, 1000) if True], [time_couplage[i] for i in range(len(time_couplage)) if i%3==1],'-o', label=f'$p={0.5}$', color=cmap(2))
ax.plot([i for i in range(1000,10001, 1000) if True], [time_couplage[i] for i in range(len(time_couplage)) if i%3==2], '-o', label=f'$p={0.8}$', color=cmap(3))
ax.legend()
ax.set_xlabel("Taille de l'instance en sommets")
ax.set_ylabel("Temps d'exécution (s)")
plt.savefig('plots/couplage_time.png', dpi=300, bbox_inches='tight')
plt.show()

fig2, ax2 = plt.subplots()
cmap = plt.get_cmap("Reds", 4) 
plt.xlim(0,11000)
plt.ylim(0,35)
ax2.set_title("Temps d'exécution moyen de l'algorithme \nglouton en fonction de n", pad=10)
ax2.plot([i for i in range(1000,10001, 1000) if True], [time_glouton[i] for i in range(len(time_glouton)) if i%3==0], '-o', label=f'$p={0.2}$', color=cmap(1))
ax2.plot([i for i in range(1000,10001, 1000) if True], [time_glouton[i] for i in range(len(time_glouton)) if i%3==1],'-o', label=f'$p={0.5}$', color=cmap(2))
ax2.plot([i for i in range(1000,10001, 1000) if True], [time_glouton[i] for i in range(len(time_glouton)) if i%3==2], '-o', label=f'$p={0.8}$', color=cmap(3))
ax2.legend()
ax2.set_xlabel("Taille de l'instance en sommets")
ax2.set_ylabel("Temps d'exécution (s)")
plt.savefig('plots/glouton_time.png', dpi=300, bbox_inches='tight')
plt.show()

[time_couplage, time_glouton, size_couplage, size_glouton] = lectureFichier("benhmark/values1_variationp.txt", 15)

for i in range(2, 6) :
    name = "benhmark/values" + str(i) + "_variationp.txt"
    [time_couplage2, time_glouton2, size_couplage2, size_glouton2] = lectureFichier(name, 15)
    for j in range (0, 15) :
        time_couplage[j] = (time_couplage[j] + time_couplage2[j])
        time_glouton[j] = (time_glouton[j] + time_glouton2[j])
        size_couplage[j] = (size_couplage[j] + size_couplage2[j])
        size_glouton[j] = (size_glouton[j] + size_glouton2[j])

for j in range (0, 15) :
    time_couplage[j] = time_couplage[j]/5
    time_glouton[j] = time_glouton[j]/5
    size_couplage[j] = size_couplage[j]/5
    size_glouton[j] = size_glouton[j]/5

fig, ax = plt.subplots(figsize=(12,5), nrows=1, ncols=3, sharey=True)
cmap = plt.get_cmap("GnBu", 3) 

plt.xlim(0,6000)
plt.ylim(0,6000)
fig.suptitle("Efficacité comparée des algorithmes")
ax[0].set_title(f'$p={0.05}$')
ax[0].plot([i for i in range(1000,5001, 1000) if True], [size_couplage[i] for i in range(len(size_couplage)) if i%3==0],'-o', label="couplage ", color=cmap(2))
ax[0].plot([i for i in range(1000,5001, 1000) if True], [size_glouton[i] for i in range(len(size_glouton)) if i%3==0], '-o', label="glouton", color=cmap(1))
# ax[0].legend()
ax[0].set_xlabel("Taille de l'instance en sommets")
ax[0].set_ylabel("Taille de la solution trouvée")
# plt.savefig('plots/efficacite_0,05_size.png', dpi=300, bbox_inches='tight')
# plt.show()

# plt.xlim(0,6000)
# plt.ylim(0,6000)
ax[1].set_title(f'$p={0.1}$', pad=10)
ax[1].plot([i for i in range(1000,5001, 1000) if True], [size_couplage[i] for i in range(len(size_couplage)) if i%3==1],'-o', label="couplage", color=cmap(2))
ax[1].plot([i for i in range(1000,5001, 1000) if True], [size_glouton[i] for i in range(len(size_glouton)) if i%3==1], '-o', label="glouton", color=cmap(1))
# ax[1].legend()
ax[1].set_xlabel("Taille de l'instance en sommets")
# ax[1].set_ylabel("Taille de la solution trouvée")
# plt.savefig('plots/efficacite_0,1_size.png', dpi=300, bbox_inches='tight')
# plt.show()

# plt.xlim(0,6000)
# plt.ylim(0,6000)
ax[2].set_title(f'$p={0.15}$', pad=10)
ax[2].plot([i for i in range(1000,5001, 1000) if True], [size_couplage[i] for i in range(len(size_couplage)) if i%3==2],'-o', label="couplage", color=cmap(2))
ax[2].plot([i for i in range(1000,5001, 1000) if True], [size_glouton[i] for i in range(len(size_glouton)) if i%3==2], '-o', label="glouton", color=cmap(1))
ax[2].legend()
ax[2].set_xlabel("Taille de l'instance en sommets")
# ax[2].set_ylabel("Taille de la solution trouvée")
plt.savefig('plots/efficacite_size.png', dpi=300, bbox_inches='tight')
plt.show()