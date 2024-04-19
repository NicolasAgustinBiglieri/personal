from persona import Persona
from cursor_del_pool import CursorDelPool
from logger_base import log

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update_Delete)
    '''
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:    
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Persona insertada: {persona}")
            return cursor.rowcount

            
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Persona actualizada: {persona}")
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Persona eliminada: {persona}")
            return cursor.rowcount



if __name__ == "__main__":
    # Insertar un registro
    persona1 = Persona(nombre="Pepona", apellido="Salamez", email="psalamez@mail.com")
    persona_insertada = PersonaDAO.insertar(persona1)
    log.debug(f"Personas insertadas: {persona_insertada}")

    # Actualizar un registro
    persona1 = Persona(nombre="sssssssssPedrossssssss", apellido="ssssssssssRodriguezssssssssss", email="sssssssssssperodriguezsssssssssss@mail.com", id_persona=20)
    persona_actualizada = PersonaDAO.actualizar(persona1)
    log.debug(f"Personas actualizadas: {persona_actualizada}")

    # Eliminar un registro
    persona1 = Persona(id_persona=18)
    eliminados = PersonaDAO.eliminar(persona1)
    log.debug(f"Personas eliminadas: {eliminados}")

    # Seleccionar registros
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
