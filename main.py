import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH
from package.fibonacci import fibonacci
from package.validator import number_valid
from package.tribonacci import tribonacci
from package.lucas import lucas
from package.rabbit import dying_rabbit as rabbit


class MainInterface:
    # Intialisation des couleurs
    blue_dark = "#1d3557"
    blue_ligth = "#a8dadc"
    blue_very_ligth = "#e0ffff"

    def __init__(self, root) -> None:
        # Configuation de base
        root.title = "Mini Python"
        root.geometry("800x400")
        # https://github.com/PapirusDevelopmentTeam/
        root.iconbitmap("python.ico")
        root.config(bg=self.blue_dark)
        # Validateur input recursive
        self.num_valid = root.register(number_valid)
        # Creation du conteneur d'onglet
        self.menu = ttk.Notebook(root)
        self.menu.pack(fill=BOTH, expand=True)

    def add_onglet(self, name, func):
        # Creation de la frame de l'onglet
        frame_generic = tk.LabelFrame(self.menu)
        frame_generic.pack()
        input_generic = tk.LabelFrame(frame_generic, bg=self.blue_ligth)
        input_generic.pack(pady=10)
        output_generic = tk.LabelFrame(frame_generic, bg=self.blue_ligth)
        output_generic.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # fonction affichage generic
        def affichage_generic():
            nombre = index_generic.get()
            index_generic.delete(0, "end")
            text_index_choosen = f"index : {nombre}"
            index_choosen.config(text=text_index_choosen,
                                 bg=self.blue_very_ligth, font=25)
            resultat = func(nombre)
            resultat_generic.config(
                text=resultat, bg=self.blue_very_ligth, font=25)

        # button,input et label generic
        label_index_generic = tk.Label(
            input_generic, text="Entrez un index entre 0 et 493"
        )
        index_generic = tk.Entry(
            input_generic, width=35, text="Quel est votre index ?",
            validate="key", validatecommand=(self.num_valid, "%P")
        )
        submit_generic = tk.Button(
            input_generic, text="Envoyer", command=affichage_generic
        )

        label_index_generic.grid(row=0, column=0, padx=10, pady=10)
        index_generic.grid(row=0, column=1, padx=10, pady=10)
        submit_generic.grid(row=0, column=2, padx=10, pady=10)
        index_choosen = tk.Label(
            output_generic, bg=self.blue_ligth, wraplength=500)
        resultat_generic = tk.Label(
            output_generic, bg=self.blue_ligth, wraplength=500)
        index_choosen.pack(padx=10, pady=10)
        resultat_generic.pack(padx=10, pady=10)
        # Ajout de la frame au menu
        self.menu.add(frame_generic, text=name)


# Creation de la base graphique
root = tk.Tk()

gui = MainInterface(root)
gui.add_onglet("fibonacci", fibonacci)
gui.add_onglet("tribonacci", tribonacci)
gui.add_onglet("lucas", lucas)
gui.add_onglet("dying_rabbit", rabbit)
root.mainloop()
