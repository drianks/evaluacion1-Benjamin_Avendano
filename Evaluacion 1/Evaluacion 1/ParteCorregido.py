class Libro:
    def __init__(self, titulo, autor, copia_stock):
        self.titulo = titulo
        self.autor = autor
        self.copia_stock = copia_stock

    def prestar(self):
        if self.copia_stock > 0:
            self.copia_stock -= 1
            return True
        return False

    def devolver(self):
        self.copia_stock += 1

    def estado(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Copias disponibles: {self.copia_stock}"


class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def registrar_libro(self, titulo, autor, copia_stock):
        if titulo not in self.catalogo:
            self.catalogo[titulo] = Libro(titulo, autor, copia_stock)
        else:
            self.catalogo[titulo].copia_stock += copia_stock

    def mostrar_catalogo(self):
        for libro in self.catalogo.values():
            print(libro.estado())

    def buscar_libro(self, titulo):
        return self.catalogo.get(titulo, None)

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.prestar():
                print(f"El préstamo se ha realizado: {titulo}.")
            else:
                print(f"No hay copias disponibles de '{titulo}'.")
        else:
            print(f"El libro '{titulo}' no se encuentra en el catálogo.")
