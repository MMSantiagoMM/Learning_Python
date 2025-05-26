simbol = input("Enter an math operation simbol")

if simbol== "*" or simbol == "/" or simbol == "+" or simbol == "-":

    try:
        num1 = int(input("Enter the first number"))
        num2 = int(input ("Enter the second number"))
        if simbol == "*":
            print(f"The result of the multiplication is:{num1*num2}")
        elif simbol == "/":
            print(f"The result of the division is:{num1/num2}")
        elif simbol == "+":
            print(f"The result of the addition is:{num1+num2}")
        elif simbol == "-":
            print(f"The result of the susbtraction is:{num1-num2}")
        else:
            print("You entered an invalid simbol")
    except:
        print("You did not entered a number")
else:
    print("You did not entered a valid simbol")







