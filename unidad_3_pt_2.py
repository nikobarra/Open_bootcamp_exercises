class coche():
    def __init__(self, puertas):
       self.puertas = puertas

    def inc_puerta(self):
        self.puertas += 1


mi_coche = coche(1)
print(f'mi coche tiene {mi_coche.puertas} puertas originalmente')
mi_coche.inc_puerta()
print (f'ahora mi coche tiene {mi_coche.puertas} puertas')
