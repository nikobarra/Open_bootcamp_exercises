import time

def hora():
    hora = time.strftime("%H:%M:%S")
    hour = int(hora[0:2])
    if hour >= 19:
        return ("Es la hora de ir a casa")
    elif hour < 19:
        falta = 19 - hour
        return(f'Faltan {falta} horas para ir a casa')