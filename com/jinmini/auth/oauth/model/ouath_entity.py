from dataclasses import dataclass

@dataclass
class AdminModel:

    username: str
    email: str
    password: str

    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username
    
    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
