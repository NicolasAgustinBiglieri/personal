#with open('prueba.txt', 'r', encoding='utf8') as archivo:
from Manejo_Archivos import Manejo_Archivos

with Manejo_Archivos('prueba.txt') as archivo:
    print(archivo.read())



