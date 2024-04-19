class Monitor:

    contador = 0

    def __init__(self, marca, tamaño) -> None:
        Monitor.contador += 1
        self._id_monitor = Monitor.contador
        self._marca = marca
        self._tamaño = tamaño

    @property
    def id_monitor(self):
        return self._id_monitor
    @id_monitor.setter
    def id_monitor(self, id_monitor):
        self._id_monitor = id_monitor
    
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property
    def tamaño(self):
        return self._tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    def __str__(self) -> str:
        return f"Monitor [Id: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamaño}\"]"
