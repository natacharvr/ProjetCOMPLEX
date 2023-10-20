import re
import matplotlib.pyplot as plt

# Lisez le fichier de données
with open("benhmark/values5_variationp.txt", "r") as file:
    lines = file.readlines()

rapport_couplage = []
rapport_glouton = []
t = []
p_values = []  # Ajout d'une liste pour stocker les valeurs de p

for line in lines:
    if line.strip():
        couplage_match = re.search(r"Taille instance couplage : (\d+)", line)
        glouton_match = re.search(r"Taille instance glouton : (\d+)", line)
        taille_p_match = re.search(r"(\d+)_(\d+\.\d+)", line)

        if taille_p_match:
            taille = int(taille_p_match.group(1))
            p = float(taille_p_match.group(2))
            t.append(taille)
            p_values.append(p)  # Enregistrement de la valeur de p
        if couplage_match:
            rapport_couplage.append(taille/int(couplage_match.group(1)))
        if glouton_match:
            rapport_glouton.append(taille/int(glouton_match.group(1)))

plt.figure(figsize=(10, 6))

# Tracer les courbes de l'algorithme de Couplage
unique_p_values = set(p_values)
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Couleurs pour les courbes de Couplage
markers = ['o', 'x', '^', 's', 'D', 'v', 'p']  # Marqueurs pour les courbes de Couplage

for idx, p_value in enumerate(unique_p_values):
    matching_indices = [i for i, value in enumerate(p_values) if value == p_value]
    label = f'Couplage (p={p_value})'  # Légende de la courbe de Couplage
    plt.plot([t[i] for i in matching_indices], [rapport_couplage[i] for i in matching_indices],
             label=label, color=colors[idx % len(colors)], marker=markers[idx % len(markers)])

# Tracer les courbes de l'algorithme Glouton
colors = ['y', 'm', 'k', 'g', 'b', 'c', 'r']  # Couleurs pour les courbes de Glouton
markers = ['s', 'D', 'v', 'p', 'o', 'x', '^']  # Marqueurs pour les courbes de Glouton

for idx, p_value in enumerate(unique_p_values):
    matching_indices = [i for i, value in enumerate(p_values) if value == p_value]
    label = f'Glouton (p={p_value})'  # Légende de la courbe de Glouton
    plt.plot([t[i] for i in matching_indices], [rapport_glouton[i] for i in matching_indices],
             label=label, color=colors[idx % len(colors)], marker=markers[idx % len(markers)])

plt.xlabel("Instances")
plt.ylabel("Rapport d'approximation")
plt.title("Rapport d'approximation des algorithmes de Couplage et Glouton en fonction de p")
plt.legend()
plt.grid(True)

plt.show()
