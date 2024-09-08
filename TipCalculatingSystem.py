def tipfunction ():
 bill = int(input("Enter the total bill : \n"))
 tip = int(input("Enter the percentage on total bill tip you want to give : \n"))
 tip = bill * tip/100
 nbil = bill + tip
 print(f"\nNew generated bill with including the tip is : ${nbil}")

