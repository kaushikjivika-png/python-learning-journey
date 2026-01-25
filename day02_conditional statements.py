# Python:

# Day 2: Conditional statements
# Topics covered: if, if-else, if-elif-else

# 1. if-statement:

x = 10
if(x>5):
    print("x is greater than 5")

# 2. if-else sttement:

y = 3
if(y%2==0):
    print("y is even")
else:
    print("y is odd")

# 3. if-elif-else statement:

z = 15
if(z<10):
    print("z is less than 10")
elif(z==10):
    print("z is equal to 10")
else:
    print("z is greater than 10")

# 4. single line if statement / Ternary operator:
# syntax:                             <var> = <val1> if <condition> else <val2>

# example 1:

fruit = input("enter fruit name:")
eat = "good" if(fruit=="apple") else("bad")
print(eat)

# example 2:

age = int(input("enter age:"))
print("eligible")if(age>=18) else print("not eligible")


# program to find largest number among three numbers:                               #  Output:
                                                                            
num1 = int(input("enter first number:"))                                         # enter first number: 45
num2 = int(input("enter second number:"))                                        # enter second number: 78
num3 = int(input("enter third number:"))                                         # enter third number: 23
if(num1>num2 and num1>num3):
    print(num1,"is the largest number")                                          #  78 is the largest number
elif(num2>num3):
    print(num2,"is the largest number")
else:

    print(num3,"is the largest number")             

# Check if Not :
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

# example:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

    
