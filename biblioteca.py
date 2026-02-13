from prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        if any(l.id_libro == libro.id_libro for l in self.libros):
            print("-Ya existe un libro con ese ID")
            return
        self.libros.append(libro)
        print("se agrega el libro de manera correcta")

    def registrar_usuario(self, usuario):
        if any(u.id_usuario == usuario.id_usuario for u in self.usuarios):
            print(" Ya existe un usuario con ese ID")
            return
        if not usuario.nombre or not usuario.email:
            print("el Nombre y el email son obligatorios")
            return
        self.usuarios.append(usuario)
        print("se registra el usuario con exito")

    def listar_libros(self):
        if not self.libros:
            print("no hya libros registrados")
            return
        for libro in self.libros:
            libro.mostrar_info()

    def prestar_libro(self, id_libro, id_usuario):
        libro = next((xlr for xlr in self.libros if xlr.id_libro == id_libro), None)
        usuario = next((drx for drx in self.usuarios if drx.id_usuario == id_usuario), None)
        
        if not libro:
            print("Libro no encontrado")
            return
        
        if not usuario:
            print(" Usuario no encontrado")
            return
        
        if not libro.disponible:
            print(" El libro ya está prestado")
            return
        
        libro.prestar()
        prestamo = Prestamo(libro, usuario)
        self.prestamos.append(prestamo)
        usuario.agregar_libro(libro)
        print("Libro prestado correctamente")
      

    def devolver_libro(self, id_libro, id_usuario):
        for prestamo in self.prestamos:
            if (
                prestamo.libro.id_libro == id_libro and 
                prestamo.usuario.id_usuario == id_usuario and 
                prestamo.fecha_devolucion is None
                ):
                prestamo.cerrar_prestamo()
                prestamo.libro.devolver()
                prestamo.usuario.devolver_libro(prestamo.libro)
                print("Libro devuelto correctamente")
                return
        print("No se encontró el préstamo")

    def listar_prestamos_activos(self):
        activos = [p for p in self.prestamos if p.esta_activo()]
        if not activos:
            print("No hay préstamos activos")
            return
        for prestamo in activos:
            prestamo.mostrar_info()

    def listar_prestamos_devueltos(self):
        devueltos = [p for p in self.prestamos if not p.esta_activo()]
        if not devueltos:
            print("No hay préstamos devueltos")
            return
        for prestamo in devueltos:
            prestamo.mostrar_info()