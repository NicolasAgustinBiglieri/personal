# Ejercicio de la Lección 3:
#
# Proporciona tu edad:
#
# 0-10: La infancia es increíble...
# 10-20: Muchos cambios y mucho estudio
# 20-30: Amor y comienza el trabajo...

edad = int(input('Proporciona tu edad: '))

if edad >= 0 and edad <= 10:
    print(f'La infancia es increíble')
elif edad >= 11 and edad <= 20:
    print(f'Muchos cambios y mucho estudio')
elif edad >= 21 and edad <= 30:
    print(f'Amor y comienza el trabajo')
else:
    print(f'Edad fuera de rango')