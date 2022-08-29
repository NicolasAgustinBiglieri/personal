# set

# los sets no tienen un orden, por lo cual no tienen índices sus elementos.
# Sus elementos no se pueden modificar pero si agregar nuevos
# No permiten elementos duplicados

# Las listas tienen elementos con índices, son modificables, se puede agregar nuevos elementos, sobreescribir, etc
# Las tuplas son inmutables, no se pueden modificar los elementos ni agregar o eliminar

# Las tuplas se definen con (); listas con []; tuplas con {}

planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
#largo
print(len(planetas))
# revisar si un elemento está presente
print('Marte' in planetas)
# agregar un elemento
planetas.add('Tierra')
print( planetas)
#no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)
# eliminar elemento posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)
# eliminar elemento sin arrojar error
planetas.discard('Júpiters')
print(planetas)
# limpiar set
planetas.clear()
print(planetas)
# eliminar el set
del planetas
print(planetas)