# Importation du module Tkinter qui permet de créer une interface graphique.
# Importation du module math qui permet de calculer l'écart-type.
# Importation du module matplotlib pour générer une courbe représentative des résultats du tirage.
# Importation du module NumPy pour utiliser np.var et np.std
from tkinter import *
import matplotlib.pyplot as plt
import math
import numpy as np



#---Définition classe principale-----------
class CalculMoyenneMediane:
    def __init__(self,  root):
        self.root = root
        self.result_text = None


    #---Calcul Moyenne, Médiane, Variance & Ecart-type------------
    def moyenne_mediane_variance_ecart_type(self, entree_utilisateur, result_text):
        try:
            Liste = [float(nombre) for nombre in entree_utilisateur.split()]
            Liste2 = [float(nombre) for nombre in entree_utilisateur.split()]
            Liste.sort()  # On trie la liste par ordre croissant.
            longueur = len(Liste)
            if longueur != 0:   # On vérifie que l'utilisateur entre au moins un nombre.
                moyenne = sum(Liste) / longueur
            
                if longueur % 2 == 0:
                    mediane = (Liste[longueur // 2 - 1] + Liste[longueur // 2]) / 2
                else:
                    mediane = Liste[longueur // 2]

                variance = sum((nombre - moyenne) ** 2 for nombre in Liste2) / longueur
                ecart_type = math.sqrt(variance)

                result_text.delete(1.0, END)  # Efface le texte précédent.
                result_text.insert(END, f"Votre moyenne est: {moyenne}\nVotre médiane est: {mediane}\nVotre variance est: {variance}\nEnfin, votre écart-type est: {ecart_type}")
            else:
                result_text.delete(1.0, END)
                result_text.insert(END, f"Votre moyenne est de 0 tout comme votre médiane !")
        except ValueError as e:  # On gère le cas où l'entrée n'est pas un nombre.
            result_text.delete(1.0, END)    # Efface le texte précédent.
            result_text.insert(END, f"Erreur de typage: {str(e)}\n")
    

     #---Afficher les graphiques------------
    def tracer_courbes(self, entree_utilisateur):
        try:
            Liste = [float(nombre) for nombre in entree_utilisateur.split()]
            plt.figure(figsize=(10, 6))

            # Graphique de la moyenne
            plt.subplot(2, 2, 1)
            plt.hist(Liste, bins=20, color="#828282", alpha=0.7)
            plt.axvline(sum(Liste) / len(Liste), color='red', linestyle='dashed', linewidth=2)  # On trace la courbe de la moyenne.
            plt.title('Moyenne')

            # Graphique de la médiane
            plt.subplot(2, 2, 2)
            plt.hist(Liste, bins=20, color="#FFA800", alpha=0.7)
            plt.axvline(sorted(Liste)[len(Liste) // 2], color='red', linestyle='dashed', linewidth=2)   # On trace la courbe de la médiane.
            plt.title('Médiane')

            # Graphique de la variance
            plt.subplot(2, 2, 3)
            plt.hist(Liste, bins=20, color="#FF00C4", alpha=0.7)
            plt.axvline(np.var(Liste), color='red', linestyle='dashed', linewidth=2)    # On trace la courbe de la variance.
            plt.title('Variance')   

            # Graphique de l'écart-type
            plt.subplot(2, 2, 4)
            plt.hist(Liste, bins=20, color="#02FF18", alpha=0.7)
            plt.axvline(np.std(Liste), color='red', linestyle='dashed', linewidth=2)    # On trace la courbe de l'écart-type.
            plt.title('Écart-type')

            plt.tight_layout()
            plt.show()

        except ValueError as e:
            print(f"Erreur de typage: {str(e)}")


    #---Fonction Tkinter------------
    def affichage_exo2(self):

        exercise_frame = Frame(self.root)
        exercise_frame.pack(pady=20)

        # Définition police du texte.
        label = Label(exercise_frame, text="Bienvenue dans l'exercice.\nCe programme va vous permettre de calculer la moyenne, la médiane,\nla variance et l'écart-type de la série des valeurs que vous entrez !", font=("Arial", 14))
        label.pack()

        entry_label = Label(exercise_frame, text="Entrez des nombres les uns à la suite des autes.\n Ils doivent être séparés par un espace:", font=("Arial", 10))
        entry_label.pack(pady=10)

        entry = Entry(exercise_frame)
        entry.pack()

        # Création bouton.
        check_button = Button(exercise_frame, text="Calculer", font=("Arial", 10), command=lambda: self.moyenne_mediane_variance_ecart_type(entry.get(), result_text))
        check_button.pack(pady=10)

        # Création bouton pour afficher les graphiques.
        graph_button = Button(exercise_frame, text="Afficher les graphiques", font=("Arial", 10), command=lambda: self.tracer_courbes(entry.get()))
        graph_button.pack(pady=10)

        # Création fenêtre pour afficher le résultat.
        result_text = Text(exercise_frame, height=10, width=60)
        result_text.pack()


