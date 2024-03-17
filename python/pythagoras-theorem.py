#Pythagoras theorem 
import math

print("\nPythagoras Calculator \n1. Find the length of A given B and C \n2. Find the length of B given A and C\n3. Find the length of C given A and B\n")

num = int(input("choose a number of the operation you'd like to calculate: "))

if num == 1:

    lengthB = float(input("Enter the length of side b: "))

    lengthC = float(input("Enter the length of side c: "))

    calc = (lengthB ** 2) + (lengthC ** 2)

    lengthA = math.sqrt(calc)

    print ("The length of side a is:", round(lengthA, 2),"(2 d.p.)")


elif num == 2:

    lengthA = float(input("Enter the length of side a: "))

    lengthC = float(input("Enter the length of side c: "))

    calc = (lengthA ** 2) + (lengthC ** 2)

    lengthB = math.sqrt(calc)

    print ("The length of side b is:", round(lengthB, 2),"(2 d.p.)")


elif num == 3:

    lengthA = float(input("Enter the length of side a: "))

    lengthB = float(input("Enter the length of side b: "))

    calc = (lengthA ** 2) + (lengthB ** 2)

    lengthC = math.sqrt(calc)

    print ("The length of side c is:", round(lengthC, 2),"(2 d.p.)")


else:
    print ("Number must be 1, 2 or 3 to perform a calculation.")