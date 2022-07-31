#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

#instalar pip install pysqlite3


#hice un CRUD completo para practicar un poco mas!

import sqlite3

#menu principal
def main():
    print('*'*50)
    print('''Ingrese que desea hacer:
          1. Ingresar nuevo Alumno
          2. Buscar Alumno
          3. mostrar todos los alumnos
          4. eliminar alumno
          5. modificar alumno
          6. Salir''')
    op = input('Su opción: ')
    if op == '1':
        print('*'*50)
        create_alumno()
    elif op == '2':
        
        search()
    elif op == '3':
        print('*'*50)
        show_all()
    elif op == '4':
        print('*'*50)
        del_alumno()
    elif op == '5':
        print('*'*50)
        update_alumno()
    else: 
        print('*'*21)
        print ('* SALIO DEL SISTEMA *')
        print('*'*21)
        


def update_alumno():
    search_id = int(input("Introduce el ID del alumno: "))
    name = input("Introduce el nombre del alumno: ").title()
    lastname = input("Introduce el apellido del alumno: ").title()
    conn = sqlite3.connect('data_base/mi_db.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE alumnos SET name = '{name}', lastname='{lastname}' WHERE id = {search_id}")
    conn.commit()
    cursor.close()
    conn.close()
    main()

def del_alumno():
    search_id = int(input("Introduce el ID del alumno: "))
    conn = sqlite3.connect('data_base/mi_db.db')
    cursor = conn.cursor()
    rows = cursor.execute(f"DELETE FROM alumnos WHERE id = '{search_id}'")
    cursor.close()
    conn.commit()
    conn.close()
    print('*'*20)
    print('* Alumno eliminado *')
    print('*'*20)
    main()
    


def show_all():
    conn = sqlite3.connect('data_base/mi_db.db')
    cursor = conn.cursor()
    rows = cursor.execute("SELECT * FROM alumnos")
    for row in rows:
        print(f'id {row[0]} nombre {row[1]} apellido {row[2]}')
    cursor.close()
    conn.close()
    main()

def search():
    search_name = input("Introduce el nombre del alumno: ").title()
    conn = sqlite3.connect('data_base/mi_db.db')
    cursor = conn.cursor()
    rows = cursor.execute(f"SELECT * FROM alumnos WHERE name = '{search_name}'")
    data = rows.fetchone() #devuelve solo un elemento
    cursor.close()
    conn.close()
    if data:
        message = f'* El alumno {data[1]} fue encontrado *'
        print('*'*len(message))
        print(message)
        print('*'*len(message))
        main()
    else:
        print('El alumno no existe')
        main()


def create_alumno():
    id = int(input("Introduce el id del alumno: "))
    name = input("Introduce el nombre del alumno: ").title()
    lastname = input("Introduce el apellido del alumno: ").title()
    
    conn = sqlite3.connect('data_base/mi_db.db')
    cursor = conn.cursor()
    query = f"INSERT INTO alumnos(id,name,lastname) VALUES ({id}, '{name}', '{lastname}')"
    rows = cursor.execute(query)
    conn.commit() #envia los datos a la bd hay que hacerlo para altas, bajas, y modificaciones
    cursor.close()
    conn.close()
    main()
    


if __name__ == '__main__':
    main()
