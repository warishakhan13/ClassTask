choice = input("Enter  choice (1.Addtion / 2.Subtraction / 3.Multiplication / 4.Division:)")
number1 = int(input("Enter first number\n"))
number2 = int(input("Enter second number\n"))
if choice == 1 :
    res = number1 + number2 
    print("Result = " ,res)
elif choice == 2 :
    res = number1 - number2 
    print("Result = " ,res)
elif choice == 3 :
    res = number1 * number2 
    print("Result = " ,res)
elif choice == 4 :
    res = number1 / number2 
    print("Result = " ,res)
else :
    print("-----")

    