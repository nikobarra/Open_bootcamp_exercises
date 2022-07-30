#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.

def area_triangulo(base, altura):
    return (base * altura) / 2

print(area_triangulo(5,6))


def area_circulo(radio):
    return 3.1416 * radio ** 2

print(area_circulo(5))
