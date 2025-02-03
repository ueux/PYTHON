menu={"pizza":220.00,
      "fries":50.00,
      "popcorn":100.50,
      "soda":30.00}
cart=[]
total=0
print("-------Menu------")
for food,price in menu.items():
    print(f"{food:10}:₹{price:.2f}")
print("------------------")
while True:
    food=input("Select an item(q to quit): ").lower()
    if food=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-----Your Order-----")
for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
print()
print(f"Total is: ₹{total}")