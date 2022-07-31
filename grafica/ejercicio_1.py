#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

#Al principio no tiene que haber una opción seleccionada.

import tkinter as tk
from tkinter import ttk
#funciones

def mostrar_seleccion():
    #genero la etiqueta
    global label_show #para que la etiqueta este disponible fuera del scope de la funcion!
    label_show = ttk.Label(window, text=f'el valor elegido es: {selected.get()}')
    label_show.grid(row=1, column=2, sticky=tk.W)
    


#genero la ventana
window = tk.Tk()
window.title("Ejercicio 1")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

#genero la etiqueta
label = ttk.Label(window, text="Ejercicio 1")
label.grid(row=0, column=0, sticky=tk.W)

#genero los radiobutton
selected = tk.StringVar()
rad_1 = ttk.Radiobutton(window, text="uno", variable=selected, value=1, command=mostrar_seleccion)
rad_1.grid(row=1, column=0, sticky=tk.W)

rad_2 = ttk.Radiobutton(window, text="dos", variable=selected, value=2, command=mostrar_seleccion)
rad_2.grid(row=2, column=0, sticky=tk.W)

rad_3 = ttk.Radiobutton(window, text="tres", variable=selected, value=3, command=mostrar_seleccion)
rad_3.grid(row=3, column=0, sticky=tk.W)

#genero el boton de reinicio
reset_btn = ttk.Button(window, text="Reset", command=lambda: (selected.set(''), label_show.grid_remove()))
reset_btn.grid(row=1, column=3, padx=5, pady=5,sticky=tk.W)


window.mainloop()


