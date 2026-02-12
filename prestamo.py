from datetime import datetime

class Prestamo:
    def __init__(self,libro,usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = datetime.now()

    def cerrar_pretamo(self):
        self.fecha_devolucion= datetime.now()