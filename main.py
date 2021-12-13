from tkinter import Tk, ttk

base = Tk() # Creation de la base

menu = ttk.Notebook(base) # Creation du conteneur d'onglets

menu.pack()

fibonaci = ttk.Frame(menu)

fibonaci.pack()