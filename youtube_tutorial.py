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

# Till here instance attributes
# ________________________________________________________________________________________________________________________________________________
#  
# From here static attributes (class attribute)

class UserClass:
    user_class_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        UserClass.user_class_count += 1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

user_class1 = UserClass("Danny", "Danny@hotmail.com") 
user_class2 = UserClass("Martin", "matin@hotmail.com")
user_class3 = UserClass("Dorine", "dorine@gmail.com")

print(UserClass.user_class_count)
print(user_class1.user_class_count)
print(user_class2.user_class_count) # omwille van de static attribute geeft dit altijd het totaal

# static attributes worden gebruikt voor counter, totals, ... of een default value
# static attributes hebben geen 'self' en kunnen dan ook niet veranderd worden
# we gebruiken een '@staticmethod' decorator

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit must be positive!")
    
    def _is_valid_amount(self, amount):
        return amount > 0
    
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. New balance: ${self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("Alice", 500)
account.deposit(600)
account.deposit(200)
print(BankAccount.is_valid_interest_rate(3))

# @staticmethod is een functie in de klasse, vergelijkbaar met private variables die niet buiten de klasse komen, maar dan voor methods

# ________________________________________________________________________________________________________________________________________________
#  
# Encapsulation

class BadBankAccount: 
    def __init__(self, balance):
        self.balance = balance

badaccount1 = BadBankAccount(0.0)
badaccount1.balance = -1

print(badaccount1.balance)

class BetterBankAccount:
    def __init__(self):
        self._balance = 0.0
    
    @property # getter
    def balance(self):
        return self._balance
    
    def deposit(self, amount): # not a setter
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount): # not a setter
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
    
account_better1 = BetterBankAccount()    
print(account_better1.balance) # mogelijk gezien @property balance
account_better1.deposit(199.0)
account_better1.withdraw(49.0)
print(account_better1.balance)
account_better1.withdraw(29.0)
print(account_better1.balance)