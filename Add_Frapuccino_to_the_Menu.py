
name = "Amo"
# Coffee Menu
menu = "Black Coffee, Espresso, Latte, Frappuccino"

#Ask Customer what they would like to order
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

#Ask Customer how many coffees they would like to order
quantity = input("How many coffees would you like?\n")

#Set the price for the coffee

if order == "Frapuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 8
else:
    print("Sorry we don't have that here.")
    price = 0

print(price)