from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_Ratones = 0

    def __init__(self, tipo_entrada, marca):
        super().__init__(tipo_entrada, marca)
        Raton.contador_Ratones += 1
        self._id_raton = Raton.contador_Ratones

    def __str__(self):
        return f'Raton: Id: {self._id_raton}, {super().__str__()}'
