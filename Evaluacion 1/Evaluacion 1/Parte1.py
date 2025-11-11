
# Ejercicio 1 — Libro y Biblioteca
# Diseña un sistema sencillo para gestionar una biblioteca. Cada libro debe tener identificados su título,
# autor y la cantidad de copias disponibles. La biblioteca debe permitir registrar nuevos libros, entregar
# libros en préstamo a los usuarios, recibir devoluciones y mostrar en cualquier momento el estado
# completo del catálogo (qué libros hay y cuántas copias quedan disponibles).
# Requerimientos funcionales
# - El sistema debe permitir registrar un nuevo libro, indicando su título, autor y número de copias
# disponibles.
# - El sistema debe permitir consultar el catálogo completo, mostrando todos los libros registrados
# junto con sus copias disponibles.
# - El sistema debe permitir buscar un libro por título para verificar si existe en la biblioteca y
# cuántas copias quedan.
# - El sistema debe permitir registrar el préstamo de un libro, disminuyendo en una unidad la
# cantidad de copias disponibles.
# - Si se intenta prestar un libro sin copias disponibles, el sistema debe informarlo claramente y no
# realizar el préstamo.
# - El sistema debe permitir registrar la devolución de un libro, aumentando en una unidad la
# cantidad de copias disponibles.
# - El sistema debe ofrecer una forma de visualizar el estado actualizado de un libro específico
# (título, autor, copias disponibles) después de préstamos y devoluciones.

class Libro:
    def __init__(self, titulo, autor, copias_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.copias_disponibles = copias_disponibles
# se define el titulo y ekl autor del libro
    def prestar(self):
        if self.copias_disponibles > 0:
            self.copias_disponibles -= 1
            return True
        else:
            return False

    def devolver(self):
        self.copias_disponibles += 1

    def estado(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Copias disponibles: {self.copias_disponibles}"
class Biblioteca:
    def __init__(self):
        self.catalogo = {}

    def registrar_libro(self, titulo, autor, copias_disponibles):
        if titulo not in self.catalogo:
            self.catalogo[titulo] = Libro(titulo, autor, copias_disponibles)
        else:
            self.catalogo[titulo].copias_disponibles += copias_disponibles

    def mostrar_catalogo(self):
        for libro in self.catalogo.values():
            print(libro.estado())

    def buscar_libro(self, titulo):
        return self.catalogo.get(titulo, None)

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.prestar():
                print(f"El prestamos se pudo realizar '{titulo}'.")
            else:
                print(f"No se encuentran copias disponible'{titulo}'.")
        else:
            print(f"El libro '{titulo}' no está registrado el libro que quiere.")

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.devolver() 
            print(f"Se realizo la devolucion '{titulo}'.")
        else:
            print(f"El libro '{titulo}' no se encuentra en la biblioteca.")
    def estado_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            print(libro.estado())
        else:            
            print(f"El libro '{titulo}' no se encuentra disponible en la biblioteca.")
#Fin de la parte uno, wiiii



          
     
