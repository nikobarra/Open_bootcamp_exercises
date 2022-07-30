#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.

#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

inicial = 2
final = 8
for num in range(inicial, final + 1):
    if num % 2 != 0:
        print(num)
    else:
        continue