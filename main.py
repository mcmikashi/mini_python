from functools import wraps
import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH
from package.fibonacci import fibonacci
from package.validator import number_valid
from package.tribonacci import tribonacci

# Intialisation des couleurs
blue_dark = "#1d3557"
blue_medium = "#457b9d"
blue_ligth = "#a8dadc"
blue_very_ligth = "#e0ffff"

# Creation de la base graphique
base = tk.Tk()
base.title("Mini Python")
base.geometry("800x400")
base.iconbitmap("python.ico")  # https://github.com/PapirusDevelopmentTeam/
base.config(bg=blue_dark)

#validateur input recursive
num_valid = base.register(number_valid)

""" les éléments de l'onglet fibonacci """

# Creation du conteneur d'onglets
menu = ttk.Notebook(base)
menu.pack(fill=BOTH, expand=True)

# Label Frame Fibonacci
frame_fibonacci = tk.LabelFrame(menu)
frame_fibonacci.pack()
input_fibonacci = tk.LabelFrame(frame_fibonacci, bg=blue_medium)
input_fibonacci.pack(pady=10)
output_fibonacci = tk.LabelFrame(frame_fibonacci, bg=blue_ligth)
output_fibonacci.pack(padx=10, pady=10, fill=BOTH, expand=True)
resultat_fibonacci = tk.Label(output_fibonacci, bg=blue_ligth, wraplength=500)
resultat_fibonacci.pack(padx=10, pady=10)


# fonction affichage
def affichage_fibonacci():
    nombre = index_fibonacci.get()
    resultat = fibonacci(nombre)
    resultat_fibonacci.config(text=resultat, bg=blue_very_ligth, font=25)


# button,input et label fibonacci
label_index_fibonacci = tk.Label(
    input_fibonacci, text="Entrez un index entre 0 et 493"
)
index_fibonacci = tk.Entry(
    input_fibonacci, width=35, validate="key",
    validatecommand=(num_valid, "%P")
)
submit_fibonacci = tk.Button(
    input_fibonacci, text="Envoyer", command=affichage_fibonacci
)

label_index_fibonacci.grid(row=0, column=0, padx=10, pady=10)
index_fibonacci.grid(row=0, column=1, padx=10, pady=10)
submit_fibonacci.grid(row=0, column=2, padx=10, pady=10)

""" les éléments de l'onglet tribonacci """

# Label Frame Tribonacci
frame_tribonacci = tk.LabelFrame(menu)
frame_tribonacci.pack()
input_tribonacci = tk.LabelFrame(frame_tribonacci, bg=blue_medium)
input_tribonacci.pack(pady=10)
output_tribonacci = tk.LabelFrame(frame_tribonacci, bg=blue_ligth)
output_tribonacci.pack(padx=10, pady=10, fill=BOTH, expand=True)

# button,input et label Tribonacci
label_index_tribonacci = tk.Label(
    input_tribonacci, text="Entrez un index entre 0 et 493"
)
index_tribonacci = tk.Entry(
    input_tribonacci, width=25, text="Quel index voulez vous ?"
)
submit_tribonacci = tk.Button(input_tribonacci, text="Envoyer", command=tribonacci)
label_index_tribonacci.grid(row=0, column=0, padx=10, pady=10)
index_tribonacci.grid(row=0, column=1, padx=10, pady=10)
submit_tribonacci.grid(row=0, column=2, padx=10, pady=10)

""" les éléments du menu """

# Ajout des onglets
menu.add(frame_fibonacci, text="Fibonacci")
menu.add(frame_tribonacci, text="Tribonacci")

base.mainloop()
