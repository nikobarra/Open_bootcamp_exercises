class alumno:
    nombre=""
    nota=0
    
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        
    def __str__(self):
        return self.nombre+" "+str(self.nota)
    
    def resultado(self):
        if self.nota>=6:
            return "Aprobado"
        else:
            return "Suspenso"
    

alumno_1 = alumno("Juan",5)
alumno_2 = alumno("Pedro",8)
print(alumno_1, alumno_1.resultado())
print (alumno_2, alumno_2.resultado())

    
    