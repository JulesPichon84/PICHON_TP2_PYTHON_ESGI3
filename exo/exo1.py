# Importation du module Tkinter qui permet de créer une interface graphique.
from tkinter import *


#---Définition classe principale-----------
class Calcul:
    def __init__(self, root):
        self.root = root

    #---Test primalité d'un nombre------------
    def testPrim(self, n, result_text):
        try:    # On vérifie si l'entrée est bien un entier positif.
            n = int(n)
            if n <= 0:
                raise ValueError("Veuillez entrer un nombre entier positif (n > 0)!")
        except ValueError as e: # On gère le cas où l'entrée n'est pas un nombre entier positif.
            result_text.delete(1.0, END)
            result_text.insert(END, f"Erreur de typage: {str(e)}\n")
            return

        j = 0
        for i in range(1, n + 1):
            if n % i == 0:
                j = j + 1
        if j == 2:
            result_text.delete(1.0, END)  # Efface le texte précédent.
            result_text.insert(END, f"Votre nombre est premier !\n")
        else:
            result_text.delete(1.0, END)  # Efface le texte précédent.
            result_text.insert(END, f"Votre nombre n'est pas premier, dommage !\n")
    
    #---Fonction Tkinter------------
    def affichage_exo1(self):

        exercise_frame = Frame(self.root)
        exercise_frame.pack(pady=20)

        # Définition police du texte.
        label = Label(exercise_frame, text="Bienvenue dans l'exercice du Nombre 1er !", font=("Arial", 14))
        label.pack()

        entry_label = Label(exercise_frame, text="Entrez un nombre afin de savoir s'il est premier:", font=("Arial", 10))
        entry_label.pack(pady=10)

        entry = Entry(exercise_frame)
        entry.pack()

        # Création bouton.
        check_button = Button(exercise_frame, text="Tester nombre", font=("Arial", 10), command=lambda: self.testPrim(entry.get(), result_text))
        check_button.pack(pady=10)

        # Création fenêtre pour afficher le résultat.
        result_text = Text(exercise_frame, height=10, width=70)
        result_text.pack()
