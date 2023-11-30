
    _____________________________   _______________.___.______________ ___ ________    _______   
    \__    ___/\______   \_____  \  \______   \__  |   |\__    ___/   |   \\_____  \   \      \  
      |    |    |     ___//  ____/   |     ___//   |   |  |    | /    ~    \/   |   \  /   |   \ 
      |    |    |    |   /       \   |    |    \____   |  |    | \    Y    /    |    \/    |    \
      |____|    |____|   \_______ \  |____|    / ______|  |____|  \___|_  /\_______  /\____|__  /
                                 \/            \/                       \/         \/         \/ 

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Lato&size=30&pause=1000&color=F70000&background=FFFFFF00&center=true&vCenter=true&multiline=true&random=false&height=100&lines=TP2+Python;Work+smarter%2C+not+harder)](https://git.io/typing-svg)

# Bienvenue dans le TP2 consacré au langage de programmation Python

## Voici l'arborescence du dossier:
    TP2
     |
     |___README.md
     |___main.py
     |___interface.py
     |___Images/
     |___Sounds/
     |
     |
     |___exo/
          |
          |___pycache
          |___exo1.py
          |___exo2_3.py
          |___exo4.py
          |___exo5.py
     

## Lors de votre arrivée dans le menu, vous trouverez plusieurs fichiers:
  1- Le fichier *main.py* représente le point d'entrée du programme, c'est par lui que tout commence.<br>
  2- Le fichier *interface.py* définit l'interface utilisateur du programme à l'aide du module Tkinter et permet d'appeler les différents exercices du TP.<br>
  3- Les dossiers *Images* et *Sound* contiennent toutes les images et les sons pour l'interface utilisateur.<br>
  4- Enfin, le dossier *exo* contient tous les exercices du TP.

Si vous souhaitez avoir un exécutable sous **Windows**, il vous suffit d'exécuter le code suivant:
  ```shell
  pyinstaller --onefile main.py
  ```

Si vous souhaitez avoir un exécutable sous **Linux**, il vous suffit d'exécuter le code suivant:
  ```shell
  pip install cx_Freeze
  ```

Créer ensuite un fichier setup.py et placez les lignes de code suivantes:
  ```python
   from cx_Freeze import setup, Executable

   setup(
        name="",
        version="",
        description="",
        executables=[Executable("main.py")])
  ```
Puis exécuter la commande suivante:
  ```shell
   python setup.py build
  ```

Volume horaire concernant le TP2:

| Tâches  | Heures |
| ------------- | ------------- |
| Développement des Scripts Python  | 10 |
| Développement du GUI  | 4 |
| Liaison du GUI aux Scripts | 2 |
| Rédaction documentation| 2 |
| Total | 18 |


> [!TIP]
> Si vous souhaitez personnalisez vous mêmes les courbes, voici deux liens menant vers la documentation des modules *seaborn* et *matplotlib*:
>  - Visit https://seaborn.pydata.org/index.html
>  - Visit https://matplotlib.org/stable/tutorials/pyplot.html


> [!WARNING]
> Si vous rencontrez des problèmes avec le programme, vous pouvez m'envoyer un message !

## Amusez-vous bien avec ce TP, et surtout n'oubliez pas d'activer le son de votre ordinateur !
