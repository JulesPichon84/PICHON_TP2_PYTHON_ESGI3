# Importation du module Tkinter qui permet de créer une interface graphique.
# Importation du module matplotlib pour générer une courbe représentative des résultats du tirage.
# Importation du module seaborn pour modifier le visuel de la courbe tracée.
# Importation du module random qui permet de générer des nombres aléatoires.
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns 
import matplotlib.pyplot as plt
import random


#---Définition classe principale-----------
class LanceurDes:
    def __init__(self, root):
        self.root = root
        self.resultats = {}
        self.result_text = None  # On stocke le widget Text.
        self.fig, self.ax = plt.subplots(figsize=(10, 5))  # Création de la figure et de l'axe.
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=BOTTOM)  # On ajoute la figure au bas de la fenêtre Tkinter.


    #---Générateur de lancés------------
    def lancer(self, nombre_tirages):
        try:    # On teste la valeur de l'âge pour qu'elle ne soit pas nulle ou < 0.
            nombre_tirages = int(nombre_tirages)
            if (nombre_tirages < 0):
                self.result_text.delete(1.0, END)   # Efface le texte précédent.
                raise ValueError("Veuillez entrer un nombre entier positif (n > 0)!") 
        except ValueError as e:     # On gère le cas où l'entrée n'est pas un nombre entier positif.
            self.result_text.delete(1.0, END)   # Efface le texte précédent.
            self.result_text.insert(END, f"Erreur de typage: {str(e)}\n")
            return
        
        self.resultats = {
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0
        }
    
        for _ in range(nombre_tirages):
            resultat = random.randint(1, 6)
            self.resultats[str(resultat)] += 1
            self.afficher_resultats_tkinter()

        # On met à jour la courbe après chaque tirage.
        self.courbe_tirages()

        # On affiche les résultats dans la fenêtre Tkinter.
        self.afficher_resultats_tkinter()


    #---Afficher les résultats dans la fenêtre tkinter------------
    def afficher_resultats_tkinter(self):

        result_str = f"Résultats des tirages:\n"
        for face, tirages in self.resultats.items():
            result_str += f"Face {face}: {tirages} tirages\n"

        total_tirages = sum(self.resultats.values())    # On calcule le nombre total de tirage par faces.
        moyenne = total_tirages / len(self.resultats)   # On calcule la moyenne de tirage pour chaque face.
       
        result_str += f"\nNombre total de tirages: {total_tirages}\n"
        result_str += f"Moyenne de tirages par face: {moyenne}"

        self.result_text.delete(1.0, END)   # Efface le texte précédent.
        self.result_text.insert(INSERT, result_str)


    #---Tracer la courbe des tirages------------
    def courbe_tirages(self):

        faces = list(self.resultats.keys())
        tirages = list(self.resultats.values())

        # Met à jour la courbe existante avec les nouveaux tirages.
        self.ax.clear()
        sns.set_theme(style="whitegrid")
        sns.lineplot(x=faces, y=tirages, marker="o", color="#FF00DC", label="Nombre de tirages", ax=self.ax)

        # Configuration du graphique.
        self.ax.set_title("Courbe représentative des tirages de dés")
        self.ax.set_xlabel("Face du dé")
        self.ax.set_ylabel("Nombre de tirages")

        # Met à jour le graphique dans la fenêtre existante.
        self.fig.canvas.draw()
    

    #---Fonction Tkinter------------
    def affichage_exo5(self):

        exercise_frame = Frame(self.root)
        exercise_frame.pack(pady=20)

        label = Label(exercise_frame, text="Bienvenue dans l'exercice du générateur de Dés !", font=("Arial", 14))
        label.pack()

        entry_label = Label(exercise_frame, text="Entrer le nombre de lancés que vous souhaitez faire:", font=("Arial", 10))
        entry_label.pack(pady=10)

        entry = Entry(exercise_frame)
        entry.pack()

        # Création bouton.
        check_button = Button(exercise_frame, text="Générer lancé", font=("Arial", 10), command=lambda: self.lancer(entry.get()))
        check_button.pack(pady=10)

        # Création fenêtre pour afficher le résultat.
        self.result_text = Text(exercise_frame, height=50, width=50)
        self.result_text.pack()

        # Création de la courbe initiale.
        self.courbe_tirages()

        # Mise à jour de la figure Tkinter.
        self.canvas.draw()

