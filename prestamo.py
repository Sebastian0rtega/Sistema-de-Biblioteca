from datetime import datetime

class Prestamo:
    def __init__(self,libro,usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = None

    def cerrar_prestamo(self):
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

    def to_dict(self):
        return {
            "id_libro": self.libro.id_libro,
            "id_usuario": self.usuario.id_usuario,
            "fecha_prestamo": self.fecha_prestamo.isoformat(),
            "fecha_devolucion": self.fecha_devolucion.isoformat() if self.fecha_devolucion else None
        }