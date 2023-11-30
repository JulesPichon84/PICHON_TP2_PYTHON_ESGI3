# Importation du module Tkinter qui permet de créer une interface graphique
# Importation du module PIL pour gérer les photos.
# Importation du module pygame pour gérer les sons.
import tkinter as tk
from PIL import Image, ImageTk
from exo.exo1 import Calcul
from exo.exo2_3 import CalculMoyenneMediane
from exo.exo4 import Age
from exo.exo5 import LanceurDes
import pygame


def exo1():
    root = tk.Tk()
    root.title("Exercice Nombre Premier")   # Titre de la fenêtre.
    root.geometry('600x400')    # Taille de la fenêtre.
    calcul_obj = Calcul(root)   # Instancier l'objet Calcul.
    calcul_obj.affichage_exo1() # Appeler la méthode affichage sur l'objet.


def exo2_3():
    root = tk.Tk()
    root.title("Exercice des calculs")   
    root.geometry('600x600')     
    calculatrice = CalculMoyenneMediane(root)   # Instancier l'objet Calcul.
    calculatrice.affichage_exo2()   # Appeler la méthode affichage sur l'objet.


def exo4():
    root = tk.Tk()
    root.title("Exercice Analyse de données d'âge")     
    root.geometry('1000x1000')    
    Statistique = Age(root)     # Instancier l'objet Lanceur.
    Statistique.affichage_exo4()    # Appeler la méthode affichage sur l'objet.


def exo5():
    root = tk.Tk()
    root.title("Exercice Lanceur dés") 
    root.geometry('1000x1000')   
    Lanceur = LanceurDes(root)  # Instancier l'objet Lanceur.
    Lanceur.affichage_exo5()    # Appeler la méthode affichage sur l'objet.


def creer_menu():
    root = tk.Tk()
    root.title("MENU PYTHON TP2 - Jules PICHON - ESGI3")
    root.geometry('600x600')


    # Redimensionne l'image de fond pour s'adapter à la taille de la fenêtre.
    def resize_image(event):   
        new_width = event.width
        new_height = event.height
        resized_image = background_image.resize((new_width, new_height), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)

    
    # Charge l'image de fond
    background_image = Image.open("Images/background.jpg") 
    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)


    # Lie la fonction de redimensionnement à l'événement de redimensionnement de la fenêtre
    root.bind("<Configure>", resize_image)


    # Initialisation de pygame.
    pygame.mixer.init()


    # Charge et joue de la musique sur la page d'accueil.
    pygame.mixer.music.load("Sounds/minecraft_main_theme.mp3")
    pygame.mixer.music.play(-1)  # Joue en boucle (-1 signifie en boucle infinie).


    def play_sound(sound_file):
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
    

    # Création d'un label pour afficher l'image de fond
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    background_label.photo = background_photo


    # Création d'un cadre (Frame) pour organiser le contenu.
    frame = tk.Frame(root)
    #frame.pack(expand=True)
    frame.grid(row=0, column=0, sticky="nsew")  # "nsew" permet l'expansion dans toutes les directions


    # Création d'un label avec le texte centré.
    label = tk.Label(frame, text="\nBienvenue dans le menu du TP2 consacré au langage de programmation Python !\nVoici la liste des exercices disponibles :\n", font=("Arial", 14))
    label.grid(row=0, column=0, columnspan=5, pady=0)  # On ajoute un espace en haut et en bas.


    # Création d'un sous-cadre (Frame) pour les boutons et les centrer.
    button_frame = tk.Frame(frame)
    button_frame.grid(row=1, column=0, columnspan=5)

    
    # Centrer le sous-cadre (Frame) des boutons.
    button_frame.grid_columnconfigure(0, weight=1)  # Permet d'étirer la colonne.


    # Création d'un bouton pour chaque exercice et association d'un son et d'une image à un bouton.
    btn1 = tk.Button(root, text="Un nombre 1er ?", command=lambda: (play_sound("Sounds/huh.mp3"), exo1()))
    btn2 = tk.Button(root, text="Des calculs scientifiques", command=lambda: (play_sound("Sounds/bully.mp3"), exo2_3()))
    btn3 = tk.Button(root, text="Etude sur l'âge de la population", command=lambda: (play_sound("Sounds/ez.mp3"), exo4()))
    btn4 = tk.Button(root, text="Générateur de lancés de dés", command=lambda: (play_sound("Sounds/xp.mp3"), exo5()))


    # On met les boutons sur la même ligne.
    btn1.grid(row=0, column=0, padx=10)
    btn2.grid(row=0, column=1, padx=10)
    btn3.grid(row=0, column=2, padx=10)
    btn4.grid(row=0, column=3, padx=10)


    # On démarre la boucle d'évènements.
    root.mainloop()


def main():
    creer_menu()

