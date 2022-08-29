a = True
b = True
resultado = a and b
print(resultado)

resultado = a or b
print(resultado)

resultado = not a
print(resultado)

# Ejercicio Valor dentro de Rango
valor = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 5

dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)

if dentroRango:
    print(f'El valor {valor} está dentro de rango')
else:
    print(f'El valor {valor} está fuera de rango')

# Para poder utilizar comillas dentro de una cadena abierta con comillas, podemos poner adelante una
# barra invertida \ para indicar que es un caracter especial y que no cierre la cadena

# Ejemplo: print('Está dentro de los 20\'s')

# ó variar entre comillas simples y dobles

# Ejemplo: print("Está dentro de los 20's")