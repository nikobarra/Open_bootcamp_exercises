class vehiculo():
    color="rojo"
    ruedas=4
    puertas=4

class coche(vehiculo):
    velocidad=200
    cilindrada = 1600
    
    def __str__(self) -> str:
        return "Coche de color {} con {} ruedas, una velocidad maxima de {} kmh y su cilindrada de {}cc".format(self.color, self.ruedas, self.velocidad, self.cilindrada)

auto = coche()
print(auto)
