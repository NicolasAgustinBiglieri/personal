
# "r" - Read - *Default value*. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exist

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# Others modes:
# "w+" to write and read
# "r+" to read, but to write too

archivo = open('prueba.txt', 'r', encoding='utf8')
print(archivo.read())

# Leer algunos caracteres (vuelvo a abrir el archivo porque al haber sido leído previamente,
# ya no quedaban caracteres por leer)
archivo = open('prueba.txt', 'r', encoding='utf8')
print(archivo.read(5))
print(archivo.read(3))

# Leer lineas completas
archivo = open('d:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
print(archivo.readline())
print(archivo.readline())

# Iterar el archivo
archivo = open('d:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
for linea in archivo:
    print(linea)

# Leer lineas
archivo = open('d:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
print(archivo.readlines())

# Acceder a una linea de la lista
archivo = open('d:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
print(archivo.readlines()[1])

# Abrimos un nuevo archivo
# (a - anexar informacion)
archivo = open('d:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se ha terminado el proiceso de leer y copiar archivos')




