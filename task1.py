print("Welcome to our tip calculator")
bill = float(input("Enter bill's cost "))
tip = int(input("Enter percentage of tip you want to give "))
people = int(input("How many pleople do you split the bill in "))

billWithTip = tip/100*bill + bill
billWithTipAndSplit = billWithTip / people

print(f"The bill's cost is: {bill} \n",
      f"The bill with tip is: {billWithTip} \n",
      f"and the cost of the bill with tip by person is: {billWithTipAndSplit}")
