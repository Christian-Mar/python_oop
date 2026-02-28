from datetime import datetime

class Person: # class
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old")

person1 = Person("Henk", 89) # object
person1.greet()

class User: 
    def __init__(self, name, age, email):
        self.name = name 
        self.age = age
        self.__email = email

    def greet(self, user):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old. You're {user.name}, {user.age} years old.")

    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self.__email
    
    def set_email(self, new_email):
        if "@" in new_email:
            self.__email = new_email

user1 = User("Henk", 89, "henk@outlook.be")
user2 = User("Nadia", 45, "nadia@gmail.com")
user1.greet(user2)

# begin variabele met _ voor een private variable die binnen de class blijft - dit is een conventie! 
# __ voor protected variables -> kan niet meer angeroepen worden buiten de class
# getters & setter zorgen ervoor dat variabelen toegankelijk zijn op een gecontroleerde manier

user1.set_email("234@675.com")
print(user1.get_email())

class Worker: 
    def __init__(self, name, age, email):
        self.name = name 
        self.age = age
        self._email = email

    @property # dit is een getter property -> voordeel dat je de functie niet hoeft aan te roepen zoals bij print(user1.get_email())
    def email(self):
        print("Email accessed")
        return self._email 
    
    @email.setter
    def email(self, new_email):
            if "@" in new_email:
                self._email = new_email
    
worker1 = Worker("John", 56, "johan@outlook.be")
print(worker1.email)

worker1.email = "this is not an email" # zal niet veranderen omdat er geen @ in voorkomt
print(worker1.email)
worker1.email = "john@gmail.com"
print(worker1.email)
