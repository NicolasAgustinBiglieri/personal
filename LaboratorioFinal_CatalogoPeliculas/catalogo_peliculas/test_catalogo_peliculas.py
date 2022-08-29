from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None  # Inicializamos la variable vacía para poder ejecutar el while
while opcion != 4:  # Mientras el usuario no proporcione "4", o sea, "salir" el programa seguirá pidiendo opciones
    try:  # Usamos try para que si el usuario no proporciona un numero, ejecute la excepcion Exception
        opcion = int(input('''
Opciones:
1. Agregar película
2. Listar películas
3. Eliminar catalogo de películas
4. Salir
Escribe tu opción (1-4):
'''))
        if opcion == 1:
            peli = input('Proporciona la película: ')
            pelicula1 = Pelicula(peli)  # Creamos el objeto con la pelicula ingresada por el usuario
            CatalogoPeliculas.agregar_pelicula(pelicula1)  # Utilizamos el metodo de CatalogoPeliculas para
            # agregar la pelicula con el objeto de tipo Pelicula
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar()
    except Exception as e:
        print(e)
        opcion = None
else:
    print('Salimos del programa')
