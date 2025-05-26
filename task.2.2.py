print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M or L: ").lower()
pizza_price = 0


if size == "s" or size == "m" or size == "l":
    if size == "s":
        pizza_price = 15
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    
        if pepperoni == "y":
            pizza_price += 2
        elif pepperoni == "n":
            print("No pepperoni added")
        else:
            print("Invalid option")

        

    elif size=="m":
        pizza_price = 20
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    
        if pepperoni == "y":
            pizza_price += 3
        elif pepperoni == "n":
            print("No pepperoni added")
        else:
            print("Invalid option")
        
    elif size =="l":
        pizza_price = 25
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
    
        if pepperoni == "y":
            pizza_price += 3
        elif pepperoni == "n":
            print("No pepperoni added")
        else:
            print("Invalid option")
    
    extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
    if extra_cheese == "y":
        pizza_price += 1
    elif extra_cheese == "n":
        print("No cheese added")
    else:
        print("Invalid option")

    print(f"You pizza cost:{pizza_price}")

else:
    print("Invalid option")


    