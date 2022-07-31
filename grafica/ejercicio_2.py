#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter as tk
from tkinter import Listbox, StringVar, ttk
#genero la ventana
window = tk.Tk()
window.title("Ejercicio 1")
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

#genero el label
label = ttk.Label(window, text="Ejercicio 1")
label.grid(row=0, column=0, sticky=tk.W)

#genero la lista con sus items
lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
lista_items = tk.StringVar(value=lista)
listbox = tk.Listbox(window,height = 6, listvariable=lista_items)
listbox.grid(row=1, column=0, sticky=tk.W)

exit_btn = ttk.Button(window, text="Salir", command=lambda: window.quit())
exit_btn.grid(row=1, column=3, padx=5, pady=5,sticky=tk.W)

window.mainloop()