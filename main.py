menu = {
    "Coffee" : 50,
    "Tea" : 20,
    "Burger" : 50,
    "Croissant" : 80,
    "Cookies" : 30,
    "Pizza" : 120,
}

print("|| Welcome to Our Cafe ||")
print("This is our Menu :- ")
print("Coffee : 50/-","\nTea : 20/-","\nBurger : 50/-","\nCroissant : 80/-","\nCookies : 30/-","\nPizza : 120/-")

item = input("Please order something : ")
print(f"{item} is added to your list")
total = 0

if item in menu:
    total += menu[item]
else:
    print("Our ordered item is not available in our menu!!")
    print("Please order something from the menu :)")


newOrder = input("U wanna order something else : (Yes/No)\n")
while newOrder == "Yes":
    print("This is our Menu :- ")
    print("Coffee : 50/-","\nTea : 20/-","\nBurger : 50/-","\nCroissant : 80/-","\nCookies : 30/-","\nPizza : 120/-")
    item_2 = input("Please order something : ")
    print(f"{item_2} is added to your list")
    if item_2 in menu:
        total += menu[item_2]
       
    else:
        print("Our ordered item is not available in our menu!!")
        print("Please order something from the menu :)")
    newOrder = " "
    newOrder = input("U wanna order something else : (Yes/No)\n")



print("Your total bill is :",total)
print(":) Thanks for Visiting :)")

