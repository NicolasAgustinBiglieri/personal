from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado


monitor1 = Monitor("Samsung", 27)
raton1 = Raton("Inalámbrico", "Logitech")
teclado1 = Teclado("Mecánico", "Roccat")

computadora1 = Computadora("Asus", monitor1, teclado1, raton1)
computadora2 = Computadora("HP", monitor1, teclado1, raton1)
orden1 = Orden([computadora1, computadora2])
print(orden1)

computadora3 = Computadora("Lenovo", monitor1, teclado1, raton1)
orden1.agregar_computadora(computadora3)
print(orden1)