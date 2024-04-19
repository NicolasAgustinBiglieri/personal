from monitor import Monitor
from teclado import Teclado
from raton import Raton

class Computadora(Monitor, Teclado, Raton):

    contador = 0

    def __init__(self, nombre,
                 monitor, 
                 teclado, 
                 raton) -> None:
        Computadora.contador += 1
        self.id_computadora = Computadora.contador
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def id_computadora(self):
        return self._id_computadora
    @id_computadora.setter
    def id_computadora(self, id_computadora):
        self._id_computadora = id_computadora

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self) -> str:
        return f'''Computadora: {self.nombre}
{self._monitor}
{self._teclado}
{self._raton}
        '''