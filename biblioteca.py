from prestamo import Prestamo
from datetime import datetime
import json
import os
from libro import Libro
from usuario import Usuario

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



    # ---------- PERSISTENCIA ----------
    def guardar_datos(self):
        with open("data/libros.json", "w", encoding="utf-8") as f:
            json.dump([l.to_dict() for l in self.libros], f, indent=4)

        with open("data/usuarios.json", "w", encoding="utf-8") as f:
            json.dump([u.to_dict() for u in self.usuarios], f, indent=4)

        with open("data/prestamos.json", "w", encoding="utf-8") as f:
            json.dump([p.to_dict() for p in self.prestamos], f, indent=4)




    def cargar_datos(self):
        if os.path.exists("libros.json") and os.path.getsize("libros.json") > 0:
            with open("libros.json", "r", encoding="utf-8") as f:
                libros_data = json.load(f)
                for l in libros_data:
                    libro = Libro(
                        l["id_libro"],
                        l["titulo"],
                        l["autor"],
                        l["fecha_creacion"]
                    )
                    libro.disponible = l["disponible"]
                    self.libros.append(libro)

        if os.path.exists("usuarios.json") and os.path.getsize("usuarios.json") > 0:
            with open("usuarios.json", "r", encoding="utf-8") as f:
                usuarios_data = json.load(f)
                for u in usuarios_data:
                    usuario = Usuario(u["id_usuario"], u["nombre"], u["email"])
                    self.usuarios.append(usuario)

        if os.path.exists("prestamos.json") and os.path.getsize("prestamos.json") > 0:
            with open("data/prestamos.json", "r", encoding="utf-8") as f:
                self.prestamos= json.load(f)
               