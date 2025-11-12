from Parte1 import Biblioteca
#inventario de libros en la biblioteca
biblioteca=Biblioteca()
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
biblioteca.estado_libro("Cronicas de Narnia")

#devolucion de libros
biblioteca.devolver_libro("Cronicas de Narnia")
print("\nEstado despues de la Devolución:")
biblioteca.estado_libro("Cronicas de Narnia")

#catalogo final de las bibliotecas y los libros
print("\nCatálogo final:")
biblioteca.mostrar_catalogo()
#fin del codigo ejercicio 1
#------------------------------------------------------------------------------#
from Parte2 import Curso
curso = Curso("Programación Orientada a Objetos")
curso.inscribir_alumno("Benjamín Abendaño")
curso.inscribir_alumno("Pedrito Pascal")
curso.inscribir_alumno("Edgard Parra")
curso.inscribir_alumno("Lilian Labbé")

print("Estado inicial del curso:")
print(curso.estado_curso())

curso.remover_alumno("Pedrito Pascal")

print("Estado después de quitar al alumno:")
print(curso.estado_curso())

curso.remover_alumno("juanito")  # Se intento quitar un alumno que no existe en el listado
print("Estado final del curso:")
print(curso.estado_curso())
#Fin del ejercicio 2 suuuu
#------------------------------------------------------------------------------#
from Parte3 import Pedido
pedido = Pedido()
pedido.agregar_item("camiseta", 29990,2)
pedido.agregar_item("Pantalones de vestir",59990, 1)
pedido.agregar_item("Zapatos", 89990, 1)

print("Detalle del pedido:")
pedido.listar_items()

total = pedido.total_pedido()
print(f"Total a pagar: {total}")
#Fin del ejercicio 3 \uwu/
#------------------------------------------------------------------------------#







