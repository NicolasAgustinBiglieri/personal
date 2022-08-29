import os


class CatalogoPeliculas:

    ruta_archivo = 'D:\\Cursos\\Python\\LaboratorioFinal_CatalogoPeliculas\\catalogo_peliculas\\peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, peli):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{peli.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catálogo de Películas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')
