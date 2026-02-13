from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca

def mostrar_menu():
    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1. Listar libros")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Ver préstamos activos")
    print("6. Ver préstamos devueltos")
    print("7. Salir")

def main():
    biblioteca = Biblioteca()

#se dejan lirbos de ejemeplo y usuarios inventados
    biblioteca.agregar_libro(Libro(1, "1984", "George Orwell", 1949))
    biblioteca.agregar_libro(Libro(2, "El Hobbit", "J.R.R. Tolkien", 1937))
    biblioteca.agregar_libro(Libro(3, "Fahrenheit 451", "Ray Bradbury", 1953))

    biblioteca.registrar_usuario(Usuario(1, "Juan Pérez", "juan@email.com"))
    biblioteca.registrar_usuario(Usuario(2, "Ana López", "ana@email.com"))

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            biblioteca.listar_libros()

        elif opcion == "2":
            try:
                id_usuario = int(input("ID usuario: "))
                nombre = input("Nombre: ")
                email = input("Email: ")
                biblioteca.registrar_usuario(Usuario(id_usuario, nombre, email))
                print("Usuario registrado correctamente")
            except ValueError:
                print("ID inválido")

        elif opcion == "3":
            try:
                id_libro = int(input("ID del libro: "))
                id_usuario = int(input("ID del usuario: "))
                biblioteca.prestar_libro(id_libro, id_usuario)
            except ValueError:
                print("Datos inválidos")

        elif opcion == "4":
            try:
                id_libro = int(input("ID del libro: "))
                id_usuario = int(input("ID del usuario: "))
                biblioteca.devolver_libro(id_libro, id_usuario)
            except ValueError:
                print("Datos inválidos")
                
        elif opcion == "5":
            biblioteca.listar_prestamos_activos()

        elif opcion == "6":
            biblioteca.listar_prestamos_devueltos()

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()