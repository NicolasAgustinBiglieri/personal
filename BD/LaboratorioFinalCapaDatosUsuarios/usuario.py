

class Usuario:

    def __init__(self, id_usuario:int = None, username:str = None, password:str = None) -> None:
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    @property
    def id_usuario(self):
        return self._id_usuario
    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = password

    def __str__(self):
        return f'Usuario: Id: {self.id_usuario}, username: {self.username}, password: {self.password}'