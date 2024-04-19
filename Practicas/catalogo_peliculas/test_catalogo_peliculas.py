from servicio.CatalogoPeliculas import CatalogoPeliculas
from dominio.Pelicula import Pelicula


eleccion = 0

while eleccion != 4:
    try:
        print("""
Bienvenidos al catálogo de películas
Dispone de las siguientes 4 opciones:
      
    1) Agregar película
    2) Listar película
    3) Eliminar archivo de películas
    4) Salir
    """)
        eleccion = int(input("Ingrese la opción deseada: "))
        if eleccion == 1:
            pelicula_elegida = input("Ingrese la película que desea agregar: ")
            pelicula = Pelicula(pelicula_elegida)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif eleccion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif eleccion == 3:
            CatalogoPeliculas.eliminar()
    except Exception as e:
        print(e)
        eleccion = 0
else:
    print('Programa finalizado.')