class Libro:
    def __init__(self,id_libro,titulo,autor,fecha_creacion):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.fecha_creacion = fecha_creacion
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible= False
            return True
        return False
    
    def devolver(self):
        self.disponible= True

    def mostrar_info(self):
        estado ="Disponible" if self.disponible else "Prestado"
        print(f"[{self.id_libro}] {self.titulo} - {self.autor} ({self.fecha_creacion}) | {estado}")