import sqlite3

# Conexión a la base de datos
conexion = sqlite3.connect("libros.db")
cursor = conexion.cursor()

def agregar_libro():
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    anio = int(input("Año de publicación: "))
    genero = input("Género: ")
    cursor.execute("INSERT INTO libros (titulo, autor, anio_publicacion, genero) VALUES (?, ?, ?, ?)",
                   (titulo, autor, anio, genero))
    conexion.commit()
    print(" Libro agregado exitosamente.")

def modificar_libro():
    id_libro = input("ID del libro a modificar: ")
    nuevo_titulo = input("Nuevo título: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_anio = int(input("Nuevo año de publicación: "))
    nuevo_genero = input("Nuevo género: ")
    cursor.execute("""
        UPDATE libros 
        SET titulo = ?, autor = ?, anio_publicacion = ?, genero = ?
        WHERE id = ?
    """, (nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero, id_libro))
    conexion.commit()
    print(" Libro modificado correctamente.")

def mostrar_libros():
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    for libro in libros:
        print(libro)

def eliminar_libro():
    id_libro = input("ID del libro a eliminar: ")
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conexion.commit()
    print(" Libro eliminado correctamente.")

def buscar_libro():
    titulo = input("Buscar libro por título (usa parte del título si quieres): ")
    cursor.execute("SELECT * FROM libros WHERE titulo LIKE ?", ('%' + titulo + '%',))
    resultados = cursor.fetchall()
    if resultados:
        for libro in resultados:
            print(libro)
    else:
        print("No se encontraron libros con ese título.")

def menu():
    while True:
        print("""
===== Menú de Gestión de Libros =====
1. Agregar libro
2. Modificar libro
3. Mostrar todos los libros
4. Eliminar libro
5. Buscar libro por título
6. Salir
""")
        opcion = input("Selecciona una opción: ")
        match opcion:
            case "1":
                agregar_libro()
            case "2":
                modificar_libro()
            case "3":
                mostrar_libros()
            case "4":
                eliminar_libro()
            case "5":
                buscar_libro()
            case "6":
                print("¡Hasta luego!")
                break
            case _:
                print(" Opción no válida. Intenta de nuevo.")

menu()
conexion.close()
