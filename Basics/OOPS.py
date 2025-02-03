import classes
from classes import Rectangle

#object - bundle of attributes and methods
#class - blueprint of object


# make class in separate file in lower-case
car1=classes.Car("Mustang", 2025, False)
car2=classes.Car("Charger", 2024, True)
print(car1)
print(car2.model)
car2.drive()

#class variables - shared by all objects, defined outside constructor,
# accessed by class name
print(classes.Car.num_car)
classes.Car.wheels+=1    #✅
print(car1.wheels) #❌
print(car2.wheels)
car1.wheels+=1  # don't
print(car1.wheels)
print(car2.wheels)

dog=classes.Dog("Scooby")
cat=classes.Cat("Garfield")
mouse=classes.Mouse("Mickey")

rabit=classes.Rabbit("Bugs")
hawk=classes.Hawk("Tony")
fish=classes.Fish("Nemo")

circle=classes.Circle("red", True, 5.0)

# #Pizza is Pizza , Circle , Shape
# shapes=[Circle(4),Square(5),Triangle(6,7),Pizza("pepperoni",15)]
# for shape in shapes:
#     print(f"{shape.area()}cm²")

print(classes.Employee.is_valid_position("Rocket Scientist"))

std1=classes.Student("Patrick", 2.0)
std2=classes.Student("Sandy", 4.0)
print(classes.Student.get_count())
print(classes.Student.get_average_gpa())

book1=classes.Book("The Hobbit", "J.R.R Tolkien", 310)
print(std1)
print(book1)
book2=classes.Book("The Hobbit", "J.R.R Tolkien", 560)
book3=classes.Book("The Hobbit", "J.R.R Tolkien", 100)
print(book2==book3)
print(book2<book3)
print(book2>book3)
print(book2+book3)
print("Hobbit"in book3)
print(book1["title"])

rect=Rectangle(3,4)
print(rect.width)
# print(rect._width)
rect.length=0
print(rect.length)
del rect.length

# Decorator - a function that extends the behaviour of another function without changing them
# def add_sprinkles(func):
#     def wrapper():
#         print("You add Srinkles")
#         func()
#     return wrapper
#without wrapper the decorator calls as @add_sprinkles executed
# @add_sprinkles
# def get_icecream():
#     print("Here is your ice cream")
def add_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("You add Srinkles")
        func(*args,**kwargs)
    return wrapper
@add_sprinkles
def get_icecream(flavour):
    print(f"Here is your {flavour} ice cream")

get_icecream("vanilla")