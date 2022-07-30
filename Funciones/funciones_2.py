#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def primo(numero):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
        return True
    else:
        return False
    
print(primo(7))