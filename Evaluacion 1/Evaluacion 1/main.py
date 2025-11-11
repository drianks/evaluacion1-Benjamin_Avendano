from Parte1 import biblioteca
#inventario de libros en la biblioteca
biblioteca=biblioteca()
biblioteca.registrar_libro("Cronicas de Narnia","C.S. Lewis",3)
biblioteca.registrar_libro("Cherlock holmes","Arthur Conan Doyle",2)
biblioteca.registrar_libro("El señor de los anillos","J.R.R. Tolkien",4)

#Se revisa el catalogo de libros en la bliblioteca
print("Catálogo que se encuentra:")
biblioteca.mostrar_catalogo()

biblioteca.prestar_libro("Cronicas de Narnia")
biblioteca.prestar_libro("Cronicas de Narnia")
biblioteca.prestar_libro("Cronicas de Narnia")
biblioteca.prestar_libro("Cronicas de Narnia") #Ya no queda stock en la biblioteca

#En que estado estan los prestamos de libros
print("\nEstado de prestamos de libros':")
biblioteca.estado("Cronicas de Narnia")

#devolucion de libros
biblioteca.devolucion_libro("Cronicas de Narnia")
print("\nEstado despues de la Devolución:")
biblioteca.estado("Cronicas de Narnia")

#catalogo final de las bibliotecas y los libros
print("\nCatálogo final:")
biblioteca.mostrar_catalogo()
#fin del codigo ejercicio 1
#------------------------------------------------------------------------------
