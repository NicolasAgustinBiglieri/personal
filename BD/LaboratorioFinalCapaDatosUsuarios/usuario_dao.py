from usuario import Usuario
from cursor_pool import CursorDelPool
from logger_base import log

class UsuarioDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update_Delete)
    '''
    _SELECCIONAR = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuario(username, password) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s"
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario=%s"

    @classmethod
    def seleccionar(cls) -> list:
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            cursor.execute(cls._INSERTAR, (usuario.username, usuario.password))
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ACTUALIZAR, (usuario.username, usuario.password, usuario.id_usuario))
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            cursor.execute(cls._ELIMINAR, (usuario.id_usuario,))
            log.debug(f'Usuario eliminado: {usuario}')
            return cursor.rowcount
            



