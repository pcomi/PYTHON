import math

#1
class Shape:
    def area(self):
        raise NotImplementedError("Area method not implemented.")

    def perimeter(self):
        raise NotImplementedError("Perimeter method not implemented.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

circle = Circle(5)
rectangle = Rectangle(4, 7)
triangle = Triangle(3, 4, 5)

#2
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self.balance

class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return "Overdraft limit exceeded"
        self.balance -= amount
        return self.balance

savings = SavingsAccount("Alice", 1000)
checking = CheckingAccount("Bob", 500)

#3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, mpg):
        super().__init__(make, model, year)
        self.mpg = mpg

    def calculate_mileage(self, miles, gallons):
        return miles / gallons if gallons else 0

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mpg):
        super().__init__(make, model, year)
        self.mpg = mpg

    def calculate_mileage(self, miles, gallons):
        return miles / gallons if gallons else 0

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity

    def get_towing_capacity(self):
        return self.towing_capacity

car = Car("Dacia", "Logan", 2022, 30)
motorcycle = Motorcycle("Yamaha", "3000", 2021, 55)
truck = Truck("Ford", "3000", 2023, 13000)

#4
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def get_info(self):
        return f"{self.name}, Salary: ${self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_total_compensation(self):
        return self.salary + self.bonus

class Engineer(Employee):
    def __init__(self, name, salary, stock_options):
        super().__init__(name, salary)
        self.stock_options = stock_options

    def calculate_total_compensation(self):
        return self.salary + self.stock_options

class Salesperson(Employee):
    def __init__(self, name, salary, commission):
        super().__init__(name, salary)
        self.commission = commission

    def calculate_total_compensation(self, sales_amount):
        return self.salary + (self.commission * sales_amount)

manager = Manager("Alice", 80000, 15000)
engineer = Engineer("Bob", 90000, 20000)
salesperson = Salesperson("Charlie", 50000, 0.10)

#5
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def get_info(self):
        return f"{self.name} lives in the {self.habitat}"

class Mammal(Animal):
    def __init__(self, name, habitat, warm_blooded=True):
        super().__init__(name, habitat)
        self.warm_blooded = warm_blooded

    def has_fur(self):
        return True

    def nurse_young(self):
        return f"{self.name} nurses its young."

class Bird(Animal):
    def __init__(self, name, habitat, can_fly=True):
        super().__init__(name, habitat)
        self.can_fly = can_fly

    def lay_eggs(self):
        return f"{self.name} lays eggs."

    def fly(self):
        return f"{self.name} can fly!" if self.can_fly else f"{self.name} cannot fly."

class Fish(Animal):
    def __init__(self, name, habitat, water_type):
        super().__init__(name, habitat)
        self.water_type = water_type

    def lay_eggs(self):
        return f"{self.name} lays eggs."

    def swim(self):
        return f"{self.name} swims in {self.water_type} water."

mammal = Mammal("Elephant", "savannah")
bird = Bird("Penguin", "Antarctica", can_fly=False)
fish = Fish("Salmon", "river", "fresh")

#6
class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            return f"{self.title} is already checked out."
        self.checked_out = True
        return f"{self.title} has been checked out."

    def return_item(self):
        if not self.checked_out:
            return f"{self.title} is already in the library."
        self.checked_out = False
        return f"{self.title} has been returned."

    def display_info(self):
        return f"Title: {self.title}, Year: {self.year}"

class Book(LibraryItem):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def display_info(self):
        return f"{super().display_info()}, Author: {self.author}, Pages: {self.pages}"

class DVD(LibraryItem):
    def __init__(self, title, year, director, duration):
        super().__init__(title, year)
        self.director = director
        self.duration = duration

    def display_info(self):
        return f"{super().display_info()}, Director: {self.director}, Duration: {self.duration} mins"

class Magazine(LibraryItem):
    def __init__(self, title, year, issue):
        super().__init__(title, year)
        self.issue = issue

    def display_info(self):
        return f"{super().display_info()}, Issue: {self.issue}"

book = Book("1984", 1949, "George Orwell", 328)
dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
magazine = Magazine("National Geographic", 2023, "June")


#1
print("circle:")
print("area:", circle.area())
print("perimeter:", circle.perimeter())

print("\nrectangle:")
print("area:", rectangle.area())
print("perimeter:", rectangle.perimeter())

print("\ntriangle:")
print("area:", triangle.area())
print("perimeter:", triangle.perimeter())

#2
print("\n")
print("savings account:")
print("initial balance:", savings.get_balance())
print("deposit 200:", savings.deposit(200))
print("withdraw 100:", savings.withdraw(100))
print("add interest:", savings.add_interest())

print("\nchecking account:")
print("initial balance:", checking.get_balance())
print("deposit 200:", checking.deposit(200))
print("withdraw 100:", checking.withdraw(100))
print("overdraft withdraw 1000:", checking.withdraw(1000))

#3
print("\n")
print("car info:", car.get_info())
print("car mileage:", car.calculate_mileage(300, 10))

print("\nmotorcycle info:", motorcycle.get_info())
print("motorcycle mileage:", motorcycle.calculate_mileage(200, 5))

print("\ntruck info:", truck.get_info())
print("truck towing capacity:", truck.get_towing_capacity())

#4
print("manager info:", manager.get_info())
print("manager total compensation:", manager.calculate_total_compensation())

print("\nengineer info:", engineer.get_info())
print("engineer total compensation:", engineer.calculate_total_compensation())

print("\nsalesperson info:", salesperson.get_info())
print("salesperson total compensation with $100,000 sales:", salesperson.calculate_total_compensation(100000))

#5
print("mammal info:", mammal.get_info())
print("mammal fur:", mammal.has_fur())
print("mammal nursing:", mammal.nurse_young())

print("\nbird info:", bird.get_info())
print("bird eggs:", bird.lay_eggs())
print("bird flight:", bird.fly())

print("\nfish info:", fish.get_info())
print("fish eggs:", fish.lay_eggs())
print("fish swimming:", fish.swim())

#6
print("book info:", book.display_info())
print("check out book:", book.check_out())
print("return book:", book.return_item())

print("\nDVD info:", dvd.display_info())
print("check out DVD:", dvd.check_out())
print("return DVD:", dvd.return_item())

print("\nmagazine info:", magazine.display_info())
print("check out magazine:", magazine.check_out())
print("return magazine:", magazine.return_item())