"""
Una CLASE es una plantilla, a partir de la cual podemos crear objetos (instancias de la clase)

La clase va a poseer Atributos y Métodos que van a establecer las características y comportamientos
de los objetos que vamos a crear
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def desplegar(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')


persona1 = Persona('Juan', 28)
persona1.desplegar()
persona2 = Persona('Karla', 30)
persona2.desplegar()
