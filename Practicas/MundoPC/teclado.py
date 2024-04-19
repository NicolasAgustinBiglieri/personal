from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contador = 0

    def __init__(self, tipoEntrada, marca) -> None:
        Teclado.contador += 1
        self._id_teclado = Teclado.contador
        DispositivoEntrada.__init__(self, tipoEntrada, marca)

    @property
    def id_teclado(self):
        return self._id_teclado
    @id_teclado.setter
    def id_teclado(self, id_teclado):
        self._id_teclado = id_teclado

    def __str__(self) -> str:
        return f"Teclado [Id: {self.id_teclado}, Tipo de teclado: {self.tipoEntrada}, Marca: {self.marca}]"
