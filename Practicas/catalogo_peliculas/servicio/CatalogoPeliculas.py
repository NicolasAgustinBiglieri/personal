import os

class CatalogoPeliculas:

    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as peliculas:
            peliculas.write(f'{pelicula.nombre}\n')
        
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as peliculas:
            print(peliculas.read())
        
    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print('Archivo eliminado')

    