from prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_libros(self):
        for libro in self.libros:
            libro.mostrar_info()

    def prestar_libro(self, id_libro, id_usuario):
        libro = next((xlr for xlr in self.libros if xlr.id_libro == id_libro), None)
        usuario = next((drx for drx in self.usuarios if drx.id_usuario == id_usuario), None)

        if not libro or not usuario:
            print("Libro o usuario no encontrado")
            return

        if libro.prestar():
            prestamo = Prestamo(libro, usuario)
            self.prestamos.append(prestamo)
            usuario.agregar_libro(libro)
            print("Libro prestado correctamente")
        else:
            print("El libro no está disponible")

    def devolver_libro(self, id_libro, id_usuario):
        for prestamo in self.prestamos:
            if prestamo.libro.id_libro == id_libro and prestamo.usuario.id_usuario == id_usuario and prestamo.fecha_devolucion is None:
                prestamo.cerrar_prestamo()
                prestamo.libro.devolver()
                prestamo.usuario.devolver_libro(prestamo.libro)
                print("Libro devuelto correctamente")
                return
        print("No se encontró el préstamo")