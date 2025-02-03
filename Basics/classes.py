from abc import abstractmethod

class Car:
    #class variables
    wheels=4
    num_car=0
    #constructor
    def __init__(self,model,year,for_sale):
        #instence variables
        self.model=model
        self.year=year
        self.for_sale=for_sale
        Car.num_car+=1
    def drive(self):
        print(f"You drive the {self.model}")

#inheritance - class Child(Parent)
class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
class Dog(Animal):
    def speak(self):
        print("WOOF")
class Cat(Animal):
    pass
class Mouse(Animal):
    pass

#multiple inheritance and multilevel
class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")
class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

#super() function
class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
class Square(Shape):
    def __init__(self,color,is_filled,length):
        super().__init__(color,is_filled)
        self.length=length
class Triangle(Shape):
    def __init__(self,color,is_filled,base,height):
        super().__init__(color,is_filled)
        self.base=base
        self.height = height


#Polymorphism
# class Shape:
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
# class Square(Shape):
#     def __init__(self,length):
#         self.length=length
#     def area(self):
#         return self.length**2
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height = height
#     def area(self):
#         return 0.5*self.base*self.height
# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         super().__init__(radius)
#         self.topping=topping

#static method - utility functions that do not need access to class data
class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    @staticmethod
    def is_valid_position(position):
        valid_positions=["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions

#class methods - for class-level data
class Student:
    count=0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=gpa
    def get_info(self):
        return f"{self.name} : {self.gpa}"
    @classmethod
    def get_count(cls):
        return f"Total no. of students: {cls.count}"
    @classmethod
    def get_average_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count}"

#Magic methods - automatically called by many Python's built-in operations.
# they allow to define or customize the behaviour of objects
class Book:
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages
    # customize the print(book1) behaviour
    def __str__(self):
        return f"{self.title} by {self.author}"
    #customize == operator
    def __eq__(self, other):
        return self.title==other.title and self.author==other.author
    #customize < operator
    def __lt__(self, other):
        return self.num_pages<other.num_pages

    # customize > operator
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # customize + operator
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    # customize in operator
    def __contains__(self, item):
        return item in self.title

    def __getitem__(self, key):
        if key=="title":
            return self.title
        elif key=="author":
            return self.author
        elif key=="num_pages":
            return self.num_pages
        else:
            return f"Key {key} not found"

#@property - decorator to use methods as attributes , getter, setter, deleter
class Rectangle:
    # _ means private protected
    def __init__(self,width,length):
        self._width=width
        self._length=length
    #getters
    @property
    def width(self):
        return f"{self._width:.2f}cm"
    @property
    def length(self):
        return f"{self._length:.2f}cm"
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print("New Width must be greater than 0")
    @length.setter
    def length(self,new_length):
        if new_length>0:
            self._length=new_length
        else:
            print("New length must be greater than 0")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @length.deleter
    def length(self):
        del self._length
        print("length has been deleted")

