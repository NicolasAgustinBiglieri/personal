class Orden:

    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = list(computadoras)

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def agregarComputadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for i in self.computadoras:
            computadoras_str += i.__str__() + '\n'

        return f'Orden: {self._idOrden}, Computadoras:\n{computadoras_str}'
