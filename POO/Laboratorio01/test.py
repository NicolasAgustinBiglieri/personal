from Raton import Raton
from Teclado import Teclado
from Monitor import *
from Computadora import *
from Orden import *


teclado1 = Teclado('usb', 'Roccat')
raton1 = Raton('usb', 'Genius')
monitor1 = Monitor('Samsung', '24 pulgadas')

teclado2 = Teclado('Bluetooth', 'Genius')
raton2 = Raton('Bluetooth', 'Logitech')
monitor2 = Monitor('LG', '21 pulgadas')

teclado3 = Teclado('No se', 'Yamaha')
raton3 = Raton('Tampoco', 'Perez')
monitor3 = Monitor('Toma Corriente', 'la tele')

computadora1 = Computadora('Personal', monitor1, teclado1, raton1)
computadora2 = Computadora('Laboral', monitor2, teclado2, raton2)
computadora3 = Computadora('PC de la abuela', monitor3, teclado3, raton3)

print(computadora1)
print(computadora2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)

orden1.agregarComputadora(computadora3)

print(orden1)