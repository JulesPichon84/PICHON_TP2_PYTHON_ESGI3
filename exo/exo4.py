# Importation du module Tkinter qui permet de créer une interface graphique.
# Importation du module matplotlib pour générer une courbe représentative des résultats du tirage.
# Importation du module seaborn pour modifier le visuel de la courbe tracée.
from tkinter import *
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#---Définition classe principale-----------
class Age:
    def __init__(self, root):
        self.root = root
        self.result_text = None
        self.Liste_age = []
        self.fig, self.ax = plt.subplots(figsize=(10, 5), tight_layout=True)
        self.canvas = None

    #---Vérifier l'âge------------
    def verif_age(self, age):
        try:    # On teste la valeur de l'âge pour qu'elle ne soit pas nulle ou < 0.
            age = int(age)
            if age < 0:
                self.result_text.delete(1.0, END)   # Efface le texte précédent.
                raise ValueError("Veuillez entrer un nombre entier positif (n > 0)!")
        except ValueError as e:     # On gère le cas où l'entrée n'est pas un nombre entier positif.
            self.result_text.delete(1.0, END)   # Efface le texte précédent.
            self.result_text.insert(END, f"Erreur de typage: {str(e)}\n")
            return

        self.Liste_age.append(age)
        self.afficher_resultats_tkinter()
        self.tracer_courbe()


    #---Afficher les résultats dans la fenêtre tkinter------------
    def afficher_resultats_tkinter(self):
        result_str = f"Résultats de l'analyse:\n"

        for age in self.Liste_age:
            result_str += f"Age: {age}\n"

        mediane = sum(self.Liste_age) // len(self.Liste_age)
        moyenne = sum(self.Liste_age) / len(self.Liste_age)

        result_str += f"\nMédiane des âges: {mediane}\n"
        result_str += f"Moyenne des âges: {moyenne}"

        self.result_text.delete(1.0, END)   # Efface le texte précédent.
        self.result_text.insert(INSERT, result_str)


    #---Tracer la courbe------------
    def tracer_courbe(self):
        
        self.ax.clear()

        # On utilise (self.Liste_age) comme données pour notre graphique.
        sns.histplot(self.Liste_age, kde=True, color="#8334FF", ax=self.ax)

        self.ax.set_title('Distribution des âges')  # Créer un titre au graphique.
        self.ax.set_xlabel('Âge (ans)')     # Donne un titre à l'axe 'x'.
        self.ax.set_ylabel('Fréquence (nb de personne)')    # Donne un titre à l'axe 'y'.

        # Si un widget de canevas (canvas) existe déjà, le détruire pour le mettre à jour
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # On créer un nouvel objet de canevas (canvas) pour afficher le graphique.
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        
        # On récupère le widget de canevas à partir de l'objet canevas.
        self.canvas_widget = self.canvas.get_tk_widget()

        # On affiche le widget de canevas dans la fenêtre principale.
        self.canvas_widget.pack()


    #---Fonction Tkinter------------
    def affichage_exo4(self):

        exercise_frame = Frame(self.root)
        exercise_frame.pack(pady=20)

        label = Label(exercise_frame, text="Bienvenue dans l'exercice d'analyse d'âge !", font=("Arial", 14))
        label.pack()

        entry_label = Label(exercise_frame, text="Entrez un age à la fois. Pour analyser les âges entrés, cliquez sur Analyser", font=("Arial", 10))
        entry_label.pack(pady=10)

        entry = Entry(exercise_frame)
        entry.pack()

        # Création bouton.
        check_button = Button(exercise_frame, text="Analyser âge", font=("Arial", 10), command=lambda: self.verif_age(entry.get()))
        check_button.pack(pady=10)

        # Création fenêtre pour afficher le résultat.
        self.result_text = Text(exercise_frame, height=15, width=50)
        self.result_text.pack()

        # Création de la courbe initiale.
        self.tracer_courbe()

        # Mise à jour de la figure Tkinter.
        self.canvas.draw()


