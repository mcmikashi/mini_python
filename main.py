import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH

# Intialisation des couleurs
blued = "#1d3557"
bluem = "#457b9d"
bluel = "#a8dadc"

# Creation de la base graphique
base = tk.Tk() 
base.title("Mini Python")
base.geometry("800x400")
base.iconbitmap('python.ico') #https://github.com/PapirusDevelopmentTeam/
base.config(bg=blued)

# Creation du conteneur d'onglets
menu = ttk.Notebook(base) 
menu.pack(fill=BOTH,expand=True)

#Label Frame Fibonacci
frame_fibonacci = tk.LabelFrame(menu)
frame_fibonacci.pack()
input_fibonacci = tk.LabelFrame(frame_fibonacci,bg=bluem)
input_fibonacci.pack(pady=10)
output_fibonacci = tk.LabelFrame(frame_fibonacci,bg=bluel)
output_fibonacci.pack(padx=10,pady=10,fill=BOTH,expand=True)

# button et input fibonacci
index_fibonacci  = tk.Entry(input_fibonacci,text="Quel est l'emplacement du chiffre fibo ?",width=25)
submit_fibonacci  = tk.Button(input_fibonacci,text="Envoyer",command=None)
index_fibonacci.grid(row=0,column=0,padx=10,pady=10)
submit_fibonacci.grid(row=0,column=1,padx=10,pady=10)



#Label Frame Tribonacci
frame_tribonacci = tk.LabelFrame(menu)
frame_tribonacci.pack()
input_tribonacci = tk.LabelFrame(frame_tribonacci,bg=bluem)
input_fibonacci.pack(pady=10)
output_tribonacci = tk.LabelFrame(frame_tribonacci,bg=bluel)
output_tribonacci.pack(padx=10,pady=10,fill=BOTH,expand=True)

# button et input Tribonacci
index_tribonacci  = tk.Entry(input_tribonacci,text="Quel est l'emplacement du chiffre fibo ?",width=25)
submit_tribonacci  = tk.Button(input_tribonacci,text="Envoyer",command=None)
index_tribonacci.grid(row=0,column=0,padx=10,pady=10)
submit_tribonacci.grid(row=0,column=1,padx=10,pady=10)


# Ajout des onglets
menu.add(frame_fibonacci,text='Fibonacci')
menu.add(frame_tribonacci,text="Tribonacci")


base.mainloop()