from computadora import Computadora

class Orden(Computadora):

    contador = 0

    def __init__(self, computadoras) -> None:
        Orden.contador += 1
        self._id_orden = Orden.contador
        self._computadoras = list(computadoras)

    @property
    def id_orden(self):
        return self._id_orden
    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden

    @property
    def computadoras(self):
        return self._computadoras
    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def __str__(self) -> str:
        computadoras_str = ""
        for computadora in self.computadoras:
            computadoras_str += computadora.__str__() + "\n"
        return f'Orden: Id {self.id_orden}\n{computadoras_str}'
    
    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

