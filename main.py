from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca

biblioteca = Biblioteca()

# Libros
biblioteca.agregar_libro(Libro(1, "1984", "George Orwell", 1949))
biblioteca.agregar_libro(Libro(2, "El Hobbit", "J.R.R. Tolkien", 1937))

# Usuarios
biblioteca.registrar_usuario(Usuario(1, "Juan Pérez", "juan@email.com"))
biblioteca.registrar_usuario(Usuario(2, "Ana López", "ana@email.com"))

# Pruebas
biblioteca.listar_libros()
biblioteca.prestar_libro(1, 1)
biblioteca.listar_libros()
biblioteca.devolver_libro(1, 1)
biblioteca.listar_libros()