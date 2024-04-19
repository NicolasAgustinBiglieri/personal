from logger_base import log

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None) -> None:
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        
    @property
    def id_persona(self):
        return self._id_persona
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return f'''
        Id: {self.id_persona}, email: {self.email},
        Nombre: {self.nombre}, Apellido: {self.apellido}
        '''

if __name__ == '__main__':
    persona1 = Persona(1, "Juan", "Lopez", "jlopez@mail.com")
    log.debug(persona1)
    persona1 = Persona(nombre="Juan", apellido="Lopez", email="jlopez@mail.com")
    log.debug(persona1)
    persona1 = Persona(id_persona=1)
    log.debug(persona1)

