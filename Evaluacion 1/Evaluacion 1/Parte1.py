### Requerimientos funcionales##
## El sistema debe permitir registrar un nuevo libro, indicando su título, autor y número de copias##
#disponibles#
##El sistema debe permitir consultar el catálogo completo, mostrando todos los libros registrados##
##junto con sus copias disponibles##
##El sistema debe permitir buscar un libro por título para verificar si existe en la biblioteca y
##cuántas copias quedan.
##El sistema debe permitir registrar el préstamo de un libro, disminuyendo en una unidad la
##cantidad de copias disponibles.
##Si se intenta prestar un libro sin copias disponibles, el sistema debe informarlo claramente y no
##realizar el préstamo.
##El sistema debe permitir registrar la devolución de un libro, aumentando en una unidad la
##cantidad de copias disponibles.
##El sistema debe ofrecer una forma de visualizar el estado actualizado de un libro específico
##(título, autor, copias disponibles) después de préstamos y devoluciones.


#Se define la categoria de libro, con sus respectivos atributos.
class libro:
    def __init__(self,titulo,autor,copia_stock):
        self.titulo = titulo
        self.autor = autor
        self.copia_stock = copia_stock

#se define el prestamos de los libros, asi mismo la verificacion de stock de prestamos.
    def prestar(selft):
        if selft.copia_stock > 0:
            selft.copia_stock -= 1
            return True
        else:
            return False
    
    def devolver_libro(selft):
        selft.copia_stock += 1
        #se registra si devolvio el libro prestado.
    def estado(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Copias disponibles: {self.copia_stock}"
 #se hace un seguimiento del estado del libro, esto para ver si corresponde la devolucion del prestamo.
class biblioteca:
    def __init__(self):
        self.catalogo = {}
    def registrar_libro(self, titulo, autor, copia_stock):
        if titulo not in self.catalogo:
            self.catalogo[titulo] = libro(titulo, autor, copia_stock)
        else:
            self.catalogo[titulo].copia_stock += copia_stock
#se muestra el catalogo de los libros que se encuentran registrados.
    def mostrar_catalogo(self):
        for libro in self.catalogo.values():
            print(libro.estado())
    def buscar_libro(self, titulo):
        return self.catalogo.get(titulo, None)
#se busca el catalogo del libro que se encuentra disponibles
    def estado(self,titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            print(libro.estado())
        else:
            print(f"El libro '{titulo}' no se encuentra en el catálogo.")

    def prestar_libro(self,titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            if libro.prestar_libro():
                print(f"El prestamo se a realizado '{titulo}'.")
            else:
                print(f"No se encuentra el libro :c, Sera para una proxima ocasión. '{titulo}'.")
        else:
            print(f"El libro '{titulo}' No encontramos lo que esta buscando :P.")
    def devolucion_libro(self,titulo):
        libro = self.buscar_libro(titulo)
        if libro:
            libro.devolver_libro()
            print(f"Gracias por su devolucion: '{titulo}'.")
        else:
            print(f"El libro '{titulo}' no se encuentra.")
#se interactua con la persona si esta los campos que se busca o no.


          
     
