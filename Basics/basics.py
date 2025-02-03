import math
import time
import random
import testModule as hk

#Variables
first_name="Harsh"
age=20
price=10.099
is_student=True
print(f"Hello {first_name} You are {age} years old")
if is_student:print("You are Student")
else:print("Not a Student")

#Type casting
print(type(price))
price=int(price)
print(type(price))
age+=1
print(age)
age=str(age)
# age+=1    #can only concatenate str (not "int") to str
age+="1"
print(age)
first_name=bool(first_name)
print(first_name)
last_name=""
last_name=bool(last_name)
if last_name:print(last_name)
else:print("Enter a last name")

# input("Enter a name ")
name=input("Enter your name: ")
# age=input("How old are you: ") #entered data is string
# age=int(age)+0
age=int(input("How Old are you"))+0
print(f"Hello {name}")
print(f"You Are {age} years old")

length=float(input("Enter Length "))
width=float(input("Enter Width "))
area=length*width
print(f"Area={area}cm²")

#operators and math functions
age**=2 #age²
length=round(length)
area=pow(length,2)
min=min(length,width)
print(round(math.pi,2))
print(math.sqrt(area))
math.ceil(width)
math.floor(width)

res=input("Would You Like Food(Y/N): ")
if res=="Y"or res=="y" and not res=="n":
    print("Have some food")
elif res=="N"or res=="n":
    print("No food for you")
else:
    print(f"{res} not valid")

#conditional expression
# X if condition else Y
res="length is even" if length%2==0 else "length is odd"
print(res)

#string methods
name="My name is HARSH"
len(name)
name.find("a")
name.rfind("Z")
name.capitalize()
name.upper()
name.lower()
name.isalpha() #true - not contain space,numbers & symbols
name.isdigit() #true - only contain digits
name.count(" ")
name.replace(" ","_")
# print(help(str)) # all methods

#string indexing - [start:end:step]
print(name[0]) # 0 1 2 3 ...
print(name[-1]) # ... -3 -2 -1
print(name[0:name.find(" ")+1])
print(name[:name.rfind(" ")])
print(name[0:])
print(name[-5:])
print(name[0:len(name):2]) # name[0] name[2] name[4] ...
print(name[::3]) # name[0] name[3] name[6] ...
print(name[::-1]) #reverse

#format specifiers - {value:flags}
a=-3000.1474
print(f"{a:+,.2f}")
print(f"{a:15}")#:(num) = allocate that many spaces
print(f"{a:015}")#:03 = allocate and zero pad that many spaces
print(f"{a:<15}")#:< = left justify
print(f"{a:>15}")#:> = right justify
print(f"{a:^15}")#:^ = center align

#loops
name=input("What is your name")
# while name=="":
#     print("You did not enter your name")
#     name=input("Enter your name")
while True:
    if(name==""):
        name=input("Enter your name")
    else:
        break
print(f"Hello {name}")
for x in range(1,11):  # 1 2 3 ... 10
    print(x)
    time.sleep(1)
# for x in reversed(range(1,11)):  # 10 9 8 ... 1
#     print(x)
for x in range(10,0,-1):  # 10 9 8 ... 1
    print(x)
    time.sleep(1)
for x in range(1,11,2): # 1 3 5 7 9
    print(x)
for x in name:
    print(x)
    print("Next letter: ",end="")

# collections -
# list[]- ordered ,mutable, allow duplicates ,
# set{}- unordered, immutable, add/remove ok , no duplicates ,
# tuple()- ordered , immutable , duplicates ok, faster

fruits=["apple","orange","banana","coconut"]
for fruit in fruits:
    print(fruit)
# print(dir(fruits)) # list methods
len(fruits)
print("apple" in fruits)
fruits[0]="pineapple"
fruits.append("strawberry")
fruits.insert(1,"pineapple")
fruits.remove("banana")
fruits.sort()
fruits.reverse()
print(fruits.index("coconut"))
print(fruits.count("pineapple"))
print(fruits)
fruits.clear()

fruits={"apple","orange","banana","coconut"}
# print(help(fruits))
for fruit in fruits:
    print(fruit)
len(fruits)
print("apple" in fruits)
fruits.add("strawberry")
fruits.add("strawberry") #only one strawberry
fruits.remove("banana")
fruits.pop() #random
print(fruits)
fruits.clear()

fruits=("apple","orange","banana","coconut","coconut")
len(fruits)
print("apple" in fruits)
print(fruits.index("coconut"))
print(fruits.count("coconut"))

#Shopping Cart
foods=[]
prices=[]
total=0
while True:
    food=input("Enter a food to buy(q to quit):")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of a {food}: "))
        foods.append(food)
        prices.append(price)
print("------Your Cart------")
for food in foods:
    print(food,end=" ")
for price in prices:
    total+=price
print()
print(f"Your total: {total}")

#2D collections
fruits=["apple","orange","banana","coconut"]
vegetables=["carrots","potatoes","tomatoes"]
meats=["chicken","fish"]
groceries=[fruits,vegetables,meats]
print(groceries)
print(groceries[0])
print(groceries[0][0])
for foods in groceries:
    for food in foods:
        print(food,end=" ")
    print()
num_pad=((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()

#dictionary - {key:value} , ordered , mutable. no duplicates
capitals={"India":"New Delhi",
          "USA":"Washington D.C",
          "China":"Beijing",
          "Russia":"Moscow"}
# print(help(capitals))
if capitals.get("japan"):
    print("Capital of Japan doesn't exit")
capitals.update({"Germany":"Berlin"})
capitals.update({"India":"Mumbai"})
capitals.pop("China")
capitals.popitem() #delete the latest inserted pair
capitals.keys() #returns an object of keys
capitals.values() # also returns an object
capitals.items() # returns am object of tuples [("",""),("",""),...]
for key in capitals:
    print(key)
for key,value in capitals.items():
    print(f"{key}:{value}")
print(capitals)

#random
# print(help(random))
options=("rock","paper","scissors")
cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.randint(2,20)
random.random() # 0-1 floating number
random.choice(options) #random element from options
random.shuffle(cards)
print(cards)

#no. guessing
low=1
high=100
ans=random.randint(low,high)
guesses=0
is_running=True
print(f"Slect a number between {low} to {high}")
while is_running:
    guess=input("Enter your guess:")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<low or guess>high:
            print("Number Out of range")
        elif guess<ans:
            print("Guess higher")
        elif guess>ans:
            print("Guess Lower")
        else:
            print("Correct")
            print(f"Number of Guesses: {guesses}")
            is_running=False
    else:
        print("Invalid guess")
        print(f"Slect a number between {low} to {high}")

#Rock Paper Scissors
options=("rock","paper","scissors")
running=True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice(rock,paper,scissors): ")
    print(f"Player:{player}")
    print(f"Computer:{computer}")
    if player == computer:
        print("It's a tie")
    elif (player == "rock" and computer == "scissors" or
          player == "paper" and computer == "rock" or
          player == "scissors" and computer == "paper"):
        print("You Win")
    else:
        print("You Lose")
    play_again=input("Play again?(y/n): ")
    if not play_again.lower()=="y":
        running=False

#dice roll
# print("\u25CF \u250C \u2500 \u2510 \u2514 \u2518")
# ● ┌ ─ ┐ └ ┘
# ┌─────────┐
# |         |
# |    ●    |
# |         |
# └─────────┘
dice_art={
    1:("┌─────────┐",
       "|         |",
       "|    ●    |",
       "|         |",
       "└─────────┘"),
    2:("┌─────────┐",
       "|         |",
       "|    ●    |",
       "|         |",
       "└─────────┘"),
    3:("┌─────────┐",
       "|         |",
       "|    ●    |",
       "|         |",
       "└─────────┘"),
    4:("┌─────────┐",
       "|         |",
       "|    ●    |",
       "|         |",
       "└─────────┘"),
    5:("┌─────────┐",
       "|         |",
       "|    ●    |",
       "|         |",
       "└─────────┘"),
    6:("┌─────────┐",
       "|         |",
       "|    ●    |",
       "|         |",
       "└─────────┘")
}
dice=[]
total=0
num_of_dice=int(input("How many dice?:"))
for num in range(num_of_dice):
    dice.append((random.randint(1,6)))
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()
for die in dice:
    total+=die
print(f"Total : {total}")

#function
def function():
    print("This is a function")
function()
def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of {amount:2f} is due : {due_date}")
display_invoice("Harsh",2000,"01/01")
def add(x,y):
    return x+y
z=add(2,3)
def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last
print(create_name("harsh","kumar"))

#positional, default args , keyword, arbitrary
def net_price(list_price,tax=0.05,discount=0):
    return list_price*(1-discount)*(1+tax)
#positional arguments follows keyword arguments
net_price(454.45,15.0,discount=4.0)
print("1","2",sep=" ") #sep is a keyword argument
#arbitrary arguments - allows passing multiple arguments
# *args - tuple
# **kwargs - dictionary - For keyword arguments
# * - unpacking operator
def add(*args):
    tot=0
    for arg in args:
        tot +=arg
    return total
def print_address(**kwargs):
    for ke,val in kwargs.items():
        print(f"{ke}:{val}")
def shipping_label(*args,**kwargs):
    print()
# we can use any name inplace of args and kwargs

#iterables - an object/collection that can return its elements one at a time,
# allowing it to be iterated over in a loop
#eg- list set tuple string dictionary
fruits={"apple","banana","orange"}
# reversed(fruits) # sets are not reversible

#Membership operators - check item in collections(string, list, ...)
# in     "apple" in fruits
# not in
grades={"Harsh":"A",
        "Gauri":"B"}
student=input("Enter the name of a student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print("Student not found")

#list comprehension - compact and easier to read than traditional loops
# [expression for value in iterable if condition]
doubles=[x*2 for x in range(1,11)]
print(doubles)
# doubles=[]
# for x in range(1,11):
#     doubles.append(x*2)
fruits=["apple","banana","orange"]
fruit_chars=[fruit[0] for fruit in fruits]
nums=[1,2,-2,-4,-1]
positive=[num for num in nums if num>=0]

#Match-case statements(switch case)
def day_of_week(day):
    match day:
        case 1:
            return"It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Not a valid day"
def is_weekend(day):
    match day:
        case "Sunday"|"Saturday":
            return True
        case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
            return False
        case _:
            return "Not a valid day"

#Modules - a file containing code you want to include
#          useful to break up a large program
#          to include a module - 'import'
# print(help("modules"))
# print(help("math"))
print(hk.square(3.3))

#Variable scope
def fun1():
    x=2  #encloced
    def fun2():
        x=3   #local
        print(x)
    fun2()
x=1  #global
fun1()