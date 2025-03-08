#UNIVERSIDAD ESTATL AMAZONICA
#TAREA 12
#NOMBRE PAMELA MORALES
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
    
    def __repr__(self):
        return f"'{self.titulo}' de {self.autor} (ISBN: {self.isbn}) - Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []
    
    def __repr__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"
    
    def listar_libros_prestados(self):
        return [libro.titulo for libro in self.libros_prestados]


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios = set()  # Conjunto para almacenar usuarios únicos
        self.prestamos = {}  # Diccionario para gestionar los préstamos
    
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")
        else:
            print(f"El libro '{libro.titulo}' ya existe en la biblioteca.")
    
    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print("El libro no existe en la biblioteca.")
    
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in [u.id_usuario for u in self.usuarios]:
            self.usuarios.add(usuario)
            print(f"Usuario {usuario.nombre} registrado exitosamente.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
    
    def dar_baja_usuario(self, id_usuario):
        usuario_a_baja = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario_a_baja:
            self.usuarios.remove(usuario_a_baja)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print("Usuario no encontrado.")
    
    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        
        if not libro:
            print(f"El libro con ISBN {isbn} no está disponible.")
            return
        if not usuario:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return
        if isbn in self.prestamos:
            print(f"El libro '{libro.titulo}' ya está prestado.")
            return
        
        # Registrar el préstamo
        usuario.libros_prestados.append(libro)
        self.prestamos[isbn] = id_usuario
        print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
    
    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        if not libro:
            print(f"El libro con ISBN {isbn} no existe.")
            return
        if isbn not in self.prestamos:
            print(f"El libro '{libro.titulo}' no está prestado.")
            return
        
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if not usuario:
            print(f"Usuario con ID {id_usuario} no registrado.")
            return
        
        if self.prestamos[isbn] == id_usuario:
            usuario.libros_prestados.remove(libro)
            del self.prestamos[isbn]
            print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
        else:
            print(f"El libro '{libro.titulo}' no fue prestado a {usuario.nombre}.")
    
    def buscar_libro(self, clave, tipo_busqueda="titulo"):
        resultados = []
        if tipo_busqueda == "titulo":
            resultados = [libro for libro in self.libros.values() if clave.lower() in libro.titulo.lower()]
        elif tipo_busqueda == "autor":
            resultados = [libro for libro in self.libros.values() if clave.lower() in libro.autor.lower()]
        elif tipo_busqueda == "categoria":
            resultados = [libro for libro in self.libros.values() if clave.lower() in libro.categoria.lower()]
        
        if resultados:
            print(f"Resultados de búsqueda por {tipo_busqueda}:")
            for libro in resultados:
                print(libro)
        else:
            print(f"No se encontraron libros con {tipo_busqueda} '{clave}'.")
    
    def listar_libros_prestados_usuario(self, id_usuario):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        if usuario:
            print(f"Libros prestados a {usuario.nombre}: {usuario.listar_libros_prestados()}")
        else:
            print(f"Usuario con ID {id_usuario} no registrado.")


# Ejemplo de uso del sistema de biblioteca

# Crear la biblioteca
biblioteca = Biblioteca()

# Crear algunos libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "12345")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "67890")
libro3 = Libro("La casa de los espíritus", "Isabel Allende", "Ficción", "11223")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana García", "002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("12345", "001")  # El Quijote a Juan Pérez
biblioteca.prestar_libro("67890", "002")  # Cien años de soledad a Ana García

# Buscar libros
biblioteca.buscar_libro("Ficción", tipo_busqueda="categoria")

# Listar libros prestados a un usuario
biblioteca.listar_libros_prestados_usuario("001")

# Devolver libros
biblioteca.devolver_libro("12345", "001")

# Eliminar un libro
biblioteca.eliminar_libro("11223")

# Dar baja de un usuario
biblioteca.dar_baja_usuario("002")
