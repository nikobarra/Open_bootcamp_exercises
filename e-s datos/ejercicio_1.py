#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

f = open("e-s datos/ejercicio_1.txt", "w")
f.write("probando guardar datos")
f.write("\n")
f.write('agrenado una nueva linea')
f.close()

