from tkinter import Tk, ttk

# Creation de la base
base = Tk() 
base.title("Mini Python")
base.geometry("800x400")
base.iconbitmap('python.ico') #https://github.com/PapirusDevelopmentTeam/

menu = ttk.Notebook(base) # Creation du conteneur d'onglets

menu.pack()

fibonaci = ttk.Frame(menu)

fibonaci.pack()

#Ajout des onglets
menu.add(fibonaci,text='fibonaci')



base.mainloop()