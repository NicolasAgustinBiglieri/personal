from usuario_dao import UsuarioDAO
from usuario import Usuario
from logger_base import log


# Bienvenido a la aplicación de manejo usuarios

eleccion = 0
while eleccion != 5:
    print('''
Elija alguna de las siguientes opciones:
1) Listar usuarios
2) Agregar usuario
3) Actualizar usuario
4) Eliminar usuario
5) Salir
    ''')
    eleccion = int(input('Elija alguna de las opciones mencionadas: '))
    if eleccion == 1:
        usuarios = UsuarioDAO.seleccionar()
        print('Usuarios encontrados:')
        for usuario in usuarios:
            log.info(usuario)


    elif eleccion == 2:
        usuario_username = str(input('Ingrese el username deseado: '))
        usuario_password = str(input('Ingrese el password deseado: '))
        usuario = Usuario(username = usuario_username, password= usuario_password)
        insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Número de usuarios insertados: {insertados}\nUsuario insertado: {usuario}')


    elif eleccion == 3:
        usuario_id_usuario = int(input('Ingrese el id del usuario a actualizar: '))
        usuario_username = str(input('Ingrese el nuevo username: '))
        usuario_password = str(input('Ingrese el nuevo password: '))
        usuario = Usuario(id_usuario = usuario_id_usuario,
                          username = usuario_username,
                          password= usuario_password)
        actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Número de usuarios actualizados: {actualizados}\nUsuario actualizados: {usuario}')


    elif eleccion == 4:
        usuario_id_usuario = int(input('Ingrese el id del usuario a eliminar: '))
        usuario = Usuario(id_usuario = usuario_id_usuario)
        eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Número de usuarios eliminados: {eliminados}\nUsuario eliminados: {usuario}')

else:
    log.info('Aplicación finalizada.')