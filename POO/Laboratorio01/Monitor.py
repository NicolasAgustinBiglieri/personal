class Monitor:

    contadorMonitores = 0

    def __init__(self, marca, tamanio):
        self._marca = marca
        self._tamanio = tamanio
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio

    def __str__(self):
        return f'Monitor: Id: {self._idMonitor}, Marca: {self.marca}, Tamaño: {self.tamanio}'

