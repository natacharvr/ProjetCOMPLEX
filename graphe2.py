import re
import matplotlib.pyplot as plt

# Lisez le fichier de données
with open("benhmark/valeursBranchement2.txt", "r") as file:
    lines = file.readlines()

i_values = []
p_values = []
temps_ameliore_1 = []
solutions_ameliore_1 = []
temps_ameliore_2 = []
solutions_ameliore_2 = []

for line in lines:
        i_p_match = re.search(r"i\s*=\s*(\d+)\s+p\s*=\s*([0-9.]+)", line)
        if i_p_match:
            i_values.append(int(i_p_match.group(1)))
            p_values.append(float(i_p_match.group(2)))
        
        temps_ameliore_1_match = re.search(r"Temps d'execution algo ameliore : ([0-9.]+)s", line)
        solution_ameliore_1_match = re.search(r"solution algo ameliore: (\d+)", line)
        temps_ameliore_2_match = re.search(r"Temps d'execution algo ameliore 2 : ([0-9.]+)s", line)
        solution_ameliore_2_match = re.search(r"solution ameliore 2: (\d+)", line)
        
        if temps_ameliore_1_match :
            temps_ameliore_1.append(float(temps_ameliore_1_match.group(1)))
        if solution_ameliore_1_match :
            solutions_ameliore_1.append(int(solution_ameliore_1_match.group(1)))
        if temps_ameliore_2_match :
            temps_ameliore_2.append(float(temps_ameliore_2_match.group(1)))
        if solution_ameliore_2_match:
            solutions_ameliore_2.append(int(solution_ameliore_2_match.group(1)))

plt.figure(figsize=(12, 6))

for p in set(p_values):
    subset_i = [i_values[i] for i, p_val in enumerate(p_values) if p_val == p]
    subset_temps_ameliore_1 = [temps_ameliore_1[i] for i, p_val in enumerate(p_values) if p_val == p]
    plt.plot(subset_i, subset_temps_ameliore_1, label=f'p={p}', marker='o')

plt.title("Temps d'exécution de l'algorithme amélioré 1 en fonction de i pour chaque p")
plt.xlabel("i")
plt.ylabel("Temps (s)")
plt.legend()
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))

for p in set(p_values):
    subset_i = [i_values[i] for i, p_val in enumerate(p_values) if p_val == p]
    subset_temps_ameliore_2 = [temps_ameliore_2[i] for i, p_val in enumerate(p_values) if p_val == p]
    plt.plot(subset_i, subset_temps_ameliore_2, label=f'p={p}', marker='o')

plt.title("Temps d'exécution de l'algorithme amélioré 2 en fonction de i pour chaque p")
plt.xlabel("i")
plt.ylabel("Temps (s)")
plt.legend()
plt.grid()
plt.show()

unique_p_values = sorted(set(p_values))

plt.figure(figsize=(12, 6))

for p in unique_p_values:
    i_values_subset = [i_values[i] for i, p_val in enumerate(p_values) if p_val == p]
    solutions_ameliore_1_subset = [solutions_ameliore_1[i] for i, p_val in enumerate(p_values) if p_val == p]
    solutions_ameliore_2_subset = [solutions_ameliore_2[i] for i, p_val in enumerate(p_values) if p_val == p]
    
    plt.plot(i_values_subset, solutions_ameliore_1_subset, label=f'p={p} - Algo 1', marker='o')
    plt.plot(i_values_subset, solutions_ameliore_2_subset, label=f'p={p} - Algo 2', marker='x')

plt.title("Comparaison des solutions retournées par chaque algorithme en fonction de i pour chaque p")
plt.xlabel("i")
plt.ylabel("Solution")
plt.legend()
plt.grid()
plt.show()
