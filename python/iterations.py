# While loops example 
name_count = 0

while name_count < 5:
     name = input("enter your name: ") 
     print(name + " is great.")
     name_count += 1
  
    
# For Loops example

for i in range (5):
     name =input('enter your name: ')
     print(name +" is great.")

#list comprehension example

names =[input("enter name: ") for i in range (5)]
[print(name + " is great.") for name in names]

