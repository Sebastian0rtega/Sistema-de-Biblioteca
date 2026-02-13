from datetime import datetime

class Prestamo:
    def __init__(self,libro,usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = None

    def cerrar_pretamo(self):
        self.fecha_devolucion= datetime.now()

    def esta_activo(self):
        return self.fecha_devolucion is None

    def mostrar_info(self):
        estado = "ACTIVO" if self.esta_activo() else "DEVUELTO"
        print(
            f"Libro: {self.libro.titulo} | "
            f"Usuario: {self.usuario.nombre} | "
            f"Prestado: {self.fecha_prestamo.strftime('%d-%m-%Y %H:%M')} | "
            f"Estado: {estado}"
        )
        if self.fecha_devolucion:
            print(
                f"Devuelto: {self.fecha_devolucion.strftime('%d-%m-%Y %H:%M')}"
            )  