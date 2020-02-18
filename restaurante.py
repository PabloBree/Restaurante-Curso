import sqlite3

def crear_bd():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()
    try:
        cursor.execute('''
            CREATE TABLE categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL)
        ''')
    except sqlite3.OperationalError:
        print("La tabla CATEGORIA ya existe")
    else:
        print("Tabla CATEGORIA creada")
    try:
        conexion.execute('''
            CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL, 
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id))
        ''')
    except sqlite3.OperationalError:
        print("La tabla PLATOS ya existe")
    else:
        print("Tabla PLATOS creada")

    cursor.commit()
    conexion.close()

def crear_categoria():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()
    try:
        cat = input("Porfavor ingrese el nombre de la categoria >")
        cursor.execute("INSERT INTO categoria VALUES(null,'{}')".format(cat))
        cursor.commit()
        cursor.close()
    except sqlite3.IntegrityError:
        print("la categoria {} ya existe\n".format(cat))
    else:
        print("Categoria {} creada correctamente".format(cat))

def mostrar_menu():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()
    cate_disp = cursor.execute("SELECT * FROM categoria").fetchall()
    for ctg in cate_disp:
        print(ctg[1])
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(ctg[0])).fetchall()
        for pt in platos:
            print('\t{}'.format(pt[1]))
    print("\n")

def agregar_plato():
    conexion = sqlite3.connect('restaurante.db')
    cursor = conexion.cursor()
    cate_disp = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Selecciona una categoria para agregar el plato")
    for cd in cate_disp:
        print("[{}] {}".format(cd[0],cd[1]))

    cate_usu = int(input(">"))

    plato = input("Porfavor ingrese el nombre del plato >\n")
    try:
        cursor.execute("INSERT INTO plato VALUES(null,'{}', {})".format(plato, cate_usu))
    except sqlite3.IntegrityError:
        print("El plato {} ya existe\n".format(plato))
    else:
        print("Plato {} creada correctamente\n".format(plato))

    conexion.commit()
    conexion.close()



while True:
    print("Bienvenidos a este restaurante")
    opcion = int(input("Introduce una opcion: \n[1] Agregar una categoria\n[2] Agregar un plato\n[3] Mostrar menu\n[4] Salir del programa\n\n>"))

    if opcion == 1:
        crear_categoria()
    elif opcion == 2:
        agregar_plato()
    elif opcion == 3:
        mostrar_menu()
    elif opcion == 4:
        print("Hasta luego!")
        break
    else:
        print("Opcion erronea.")
