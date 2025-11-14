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
curso.inscribir_alumno("Pedrito pascal")
curso.inscribir_alumno("Benjamin Avendaño")
curso.inscribir_alumno("Francisca torre")
curso.inscribir_alumno("Lilian Labbé")

print("Estado inicial del curso:")
print(curso.estado_curso())

curso.remover_alumno("Lilian Labbé")

print("Estado después de remover un alumno:")
print(curso.estado_curso())

# Intento de remover alumno no inscrito
curso.remover_alumno("Camila Soto")
print("Estado final del curso:")
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
pedido.agregar_item("Camisa", 15990, 2)
pedido.agregar_item("Pantalones", 39990, 1)
pedido.agregar_item("Zapatos", 79990, 1)

print("Detalle del pedido:")
pedido.listar_items()

total = pedido.total_pedido()
print(f"Total a pagar: {total}")
# Fin del tercer ejercicio \uwu/
#------------------------------------------------------------------------------#
from Parte4 import Sensor
# Probar el sistema de sensor de mediciones ambientales
nombre_sensor = input("Ingrese el nombre del sensor: ")
sensor = Sensor(nombre_sensor)

while True:
    valor = input("Ingrese una medición (o 'fin' para terminar): ")
    if valor.lower() == "fin":
        break
    else:
        sensor.agregar_medicion(float(valor))
sensor.mostrar_resumen()
# Fin del ejercicio 4 _-(-.-)_--
#------------------------------------------------------------------------------#
from Parte5 import Catalogo

# Ejemplo de uso

catalogo = Catalogo()
catalogo.registrar_pelicula("Tron", "Ciencia Ficción", 2010)
catalogo.registrar_pelicula("El niño con el pijama de rayas", "Drama", 2008)
catalogo.registrar_pelicula("V de venganza", "Acción / Drama", 2006)
catalogo.registrar_pelicula("kung fu panda", "Ciencia Ficción ", 2008)
catalogo.registrar_pelicula("Demon slayer", "Animacion", 2025)
catalogo.registrar_pelicula("jujutsu kaisen pelicula", "Ciencia Ficción / animacion", 2021)

print("Catálogo completo:")
catalogo.mostrar_catalogo()

titulo_buscar = "Inception"
pelicula_encontrada = catalogo.buscar_pelicula(titulo_buscar)
if pelicula_encontrada:
    print(f"\nPelícula encontrada: {pelicula_encontrada.informacion()}")
else:
    print(f"\nLa película '{titulo_buscar}' no se encuentra en el catálogo.")

genero_filtrar = "Ciencia Ficción"
peliculas_filtradas = catalogo.filtrar_por_genero(genero_filtrar)
if peliculas_filtradas:
    print(f"\nPelículas del género '{genero_filtrar}':")
    for pelicula in peliculas_filtradas:
        print(pelicula.informacion())
else:
    print(f"\nNo se encontraron películas del género '{genero_filtrar}'.")
#Fin del código
#Fin de la parte cinco (*-*)
#------------------------------------------------------------------------------#
from parte6 import SistemaUsuarios

# Modo de uso del sistema de usuarios y autenticación simple
sistema = SistemaUsuarios()

# Registrar usuarios
sistema.registrar_usuario("Lolito", "1234")
sistema.registrar_usuario("Peditro", "abcd")
sistema.registrar_usuario("Lolito", "9999")  # Intento duplicado

# Iniciar sesión
sistema.iniciar_sesion("Lolito", "1234")     # Correcto
sistema.iniciar_sesion("Juanito", "1234")     # Contraseña incorrecta
sistema.iniciar_sesion("Pedrito", "qwerty")  # Usuario no existe

# Consultar si un usuario existe
sistema.usuario_registrado("Pedrito")
sistema.usuario_registrado("Juanito")

#Fin del ejercicio 6 (^_^)
#------------------------------------------------------------------------------#
from Parte7 import Agenda
agenda = Agenda()
print(agenda.agregar_contacto("Juanito", "1234567890", "juanito@mail.cl"))
print(agenda.agregar_contacto("Benjamin Avendaño", "9876543210", "benjamin@mail.cl"))
print(agenda.agregar_contacto("Pedrito", "1112223333", "Pedrito@mail.cl"))
print("\nListado de contactos:")
agenda.mostrar_contactos()
print("\nBúsqueda de contacto 'Juanito':")
print(agenda.buscar_contacto("Juanito"))
print("\nBúsqueda de contacto 'Franciasca torre':")
print(agenda.buscar_contacto("Franciasca torre"))
print("\nEliminación de contacto 'Benjamin Avendaño':")
print(agenda.eliminar_contacto("Benjamin Avendaño"))
print("\nEliminación de contacto 'Francisca torre':")
print(agenda.eliminar_contacto("Francisca torre"))
print("\nListado de contactos actualizado:")
agenda.mostrar_contactos()
#Fin del código y todos los ejercicios









