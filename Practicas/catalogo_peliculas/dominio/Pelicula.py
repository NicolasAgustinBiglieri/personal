class Pelicula:

    def __init__(self, nombre) -> None:
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self) -> str:
        return f'{self.nombre}'
    