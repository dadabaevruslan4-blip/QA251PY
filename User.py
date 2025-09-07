class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._login_attempts = 0

    @property
    def password(self):
        raise AttributeError("Password is not readable")
    @password.setter
    def password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("Password must be at least 8 characters")
        self.__password = new_password
    def verify_password(self, password):
        self._login_attempts += 1
        return self.__password == password
#Использование класса
user = User("alex", "secret123")
#print(user.__password) # Вызовет ошибку - нет доступа
#user.password # Вызовет AttributeError
#user.password = "newsecret" # Работает, проходит валидацию
user.password = "weak" # Вызовет ValueError