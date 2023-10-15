#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void genererInstance(int size, float proba, char* file_name) {
    /*
        Génère un fichier file_name contenant la description d'un graphe de size sommet, dont chaque arrête a une probabilité proba, comprise entre 0 et 1 d'être ajoutée.
    */
    
    FILE* file = fopen(file_name, "w"); // Crée un fichier dans le dossier courant
    fprintf(file, "Nombre de sommets\n");
    fprintf(file, "%d\n", size);
    fprintf(file, "Sommets\n");

    // Ecrit un nom de sommet par ligne
    for (int i=0; i<size; i++) {
        fprintf(file, "%d\n",i);
    }

    // Début de la liste d'aretes
    fprintf(file, "Aretes\n");

    float r;
    int cpt = 0; // Sert à compter le nombre d'aretes générées

    //Pour chaque couple d'aretes, générer un float aléatoire
    // S'il est inférieur à proba, alors on ajoute l'arete au fichier
    for (int i=0; i<size; i++) {
        for (int j=i+1; j<size; j++) {
            r = (float)rand()/(float)RAND_MAX;
            if (r < proba) {
                fprintf(file, "%d %d\n", i, j);
                cpt++;
            }

        }
    }
    // On écrit le nombre d'aretes
    fprintf(file, "Nombre d arretes\n");
    fprintf(file, "%d\n", cpt);
    fclose(file);


}

int main() {
    printf("Je tourne !");
    srand(time(NULL));
    char name[50];
    // i représente le nombre de sommets de l'instance générée
    for (int i=1000; i<=10001; i+=1000) {
        // j est la probabilité de présence d'une arete
        for (float j = 0.2; j<=1; j+=0.2) {
            //Tous les noms de fichiers sont de la forme "nombreDeSommets_ProbabiliteDUneArete"
            sprintf(name, "%d_%.1f", i, j);

            //On génère le fichier
            genererInstance(i, j, name);
        }
    }
    

    return 0;
}