calificacionNum = float(input('Proporciona un valor entre 0 y 10: '))
calificacionStr = None

if calificacionNum >= 9 and calificacionNum < 10:
    calificacionStr = 'A'
elif calificacionNum >= 8 and calificacionNum < 9:
    calificacionStr = 'B'
elif calificacionNum >= 7 and calificacionNum < 8:
    calificacionStr = 'C'
elif calificacionNum >= 6 and calificacionNum < 7:
    calificacionStr = 'D'
elif calificacionNum >= 0 and calificacionNum < 6:
    calificacionStr = 'F'
else:
    calificacionStr = 'Calificación fuera de rango'
print(f'Tu calificación {calificacionNum} es equivalente a {calificacionStr}')