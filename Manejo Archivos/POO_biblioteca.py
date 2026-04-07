class autor:
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"El autor es: {self.nombre}"
    

class libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
    
    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"
    

class biblioteca:
    def __init__(self):
        self.libros = []

    def añadir_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self): 
        if not self.libros:
            return "La biblioteca está vacía"
        return "\n".join(str(libro) for libro in self.libros)


# autores 
autor1 = autor("Paul Delgado", "19 de agosto del 2005")
autor2 = autor("Koraima Merchan", "04 de abril del 2005")

# libros
libro1 = libro("Los tres cerditos", autor1, "2016")
libro2 = libro("Gorgonita", autor2, "2010")

mi_biblioteca = biblioteca()
mi_biblioteca.añadir_libro(libro1)
mi_biblioteca.añadir_libro(libro2)

print(mi_biblioteca.mostrar_libros())
