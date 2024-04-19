from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):

    contador = 0

    def __init__(self, tipoEntrada, marca) -> None:
        Raton.contador += 1
        self._id_raton = Raton.contador
        DispositivoEntrada.__init__(self, tipoEntrada, marca)

    @property
    def id_raton(self):
        return self._id_raton
    @id_raton.setter
    def id_raton(self, id_raton):
        self._id_raton = id_raton

    def __str__(self) -> str:
        return f"Raton [Id: {self.id_raton}, Tipo de entrada: {self.tipoEntrada}, Marca: {self.marca}]"
