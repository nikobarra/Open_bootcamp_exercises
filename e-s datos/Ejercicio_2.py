#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def mostrar(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Color: ", self.color)
    def guardar(self):
        f = open("e-s datos/ejercicio_2.txt", "a")
        f.write(self.marca)
        f.write("\n")
        f.write(self.modelo)
        f.write("\n")
        f.write(self.color)
        f.close()
    def cargar(self):
        f = open("e-s datos/ejercicio_2.txt", "r")
        self.marca = f.readline()
        self.modelo = f.readline()
        self.color = f.readline()
        f.close()
        self.mostrar()

auto = Vehiculo("Ford", "Mustang", "Rojo")
auto_1 = Vehiculo("Chevrolet", "Camaro", "gris")

auto.guardar()
auto_1.guardar()

auto_1.cargar()

auto.cargar()

#auto.mostrar()