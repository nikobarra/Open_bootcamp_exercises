import pickle

from bs4 import MarkupResemblesLocatorWarning

class Vehiculo():
    marca = ""
    year = ""
    color = ""
    
    def __init__(self, marca, year, color):
        self.marca = marca
        self.year = year
        self.color = color
        
""" auto = Vehiculo("Ford", "Mustang", "Rojo")
f = open("e-s datos/ejercicio_2.bin", "wb")
        
pickle.dump(auto, f)
f.close()
 """ #guardo el objeto auto en el archivo ejercicio_2.bin



f = open("e-s datos/ejercicio_2.bin", "rb")
auto = pickle.load(f)
f.close()
print (auto.marca)
# abro el archivo ejercicio_2.bin y lo cargo en auto
