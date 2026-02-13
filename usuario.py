class Usuario:
    def __init__(self,id_usuario,nombre,email):
        self.id_usuario = id_usuario
        self.nombre = nombre.strip()
        self.email = email.strip()
        self.libros_prestados = []

    def agregar_libro(self,libro):
        if libro not in self.libros_prestados:
            self.libros_prestados.append(libro)

    def devolver_libro(self,libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        
    def mostrar_info(self):
        print(f"[{self.id_usuario}] {self.nombre} - {self.email}")
        print(f"Libros prestados: {len(self.libros_pretados)}")