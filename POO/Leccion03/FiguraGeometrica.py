class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    def __str__(self):
        return f'Alto: {self._alto}, Ancho: {self._ancho}'

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho


class Color:
    def __init__(self, color):
        self._color = color

    def __str__(self):
        return f'Color: {self._color}'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

    def calculoAreaCuadrado(self):
        return self._alto * self._ancho


class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'

    def calculoAreaRectangulo(self):
        return self._alto * self._ancho
