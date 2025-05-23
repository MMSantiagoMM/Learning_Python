print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M or L: ").lower
#pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
pizza_price = 0


if size == "S" or size == "M" or size == "L":
    if size == "S":
        pizza_price = 15
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower
    
        if pepperoni == "Y":
            pizza_price += 2
        elif pepperoni == "N":
            print("No pepperoni added")
        else:
            print("Invalid option")
    elif size=="M":
        pizza_price = 20
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower
    
        if pepperoni == "Y":
            pizza_price += 3
        elif pepperoni == "N":
            print("No pepperoni added")
        else:
            print("Invalid option")
        
    elif size =="L":
        pizza_price = 25
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower
    
        if pepperoni == "Y":
            pizza_price += 3
        elif pepperoni == "N":
            print("No pepperoni added")
        else:
            print("Invalid option")
else:
    print("Invalid option")


    print(f"You pizza cost:{pizza_price}")