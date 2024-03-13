num1 =int(input("enter a number please: "))
num2 =int(input("enter another number please: "))


addition = print("+")
subtraction =print("-")
multiplication=print("*")
divide=print("/")


operation=input("Enter the operator: ")

if operation == "+":
    result =int(num1) + int(num2)
    print("sum: ", result)
    
elif operation == "-":
    result =int(num1) - int(num2)
    print("sum: ", result)
    
elif operation == "*":
    result =int(num1) * int(num2)
    print("sum: ", result)

elif operation == "/":
    result =int(num1) / int(num2)
    print("sum: ", result)

else: 
    print("Invalid operation being used")