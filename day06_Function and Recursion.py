# Python:

# Day 6: Python Function and Recursion
# Topics covered: Function definition, Types of Function, Function calling, Parameters and Arguments, Default arguments, Recursion, Practice problems.

# 1. Function Definition:

# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# In Python, a function is defined using the def keyword, followed by the function name and parentheses ().
""" syntax of function is:
def function_name(parameters):
    #code to be executed
function_name() #calling the function """

# Example:

def cal_val(a,b):                                           
    diff = a-b
    print(diff)
    return diff
cal_val(2,4)

cal_val(5,3)

# 2. Types of Function:

# Built-in Function: Functions that are pre-defined in Python.
# Example: print(), len(), type(), int(), str(), etc.

# User-defined Function: Functions that are defined by the user to perform specific tasks.
# Example: cal_val() function defined above.

# 3. Function Calling:
# A function is called by using its name followed by parentheses ().
# Example: cal_val(2,4) calls the cal_val function with arguments 2 and 4.

# 4. Parameters and Arguments:
# Parameters are the variables listed inside the parentheses in the function definition.
# Arguments are the values that are sent to the function when it is called.

# Example:

def add(x, y):  # x and y are parameters
    return x + y

# 4. Default Arguments:
# Default arguments are the values that are assigned to the parameters of a function when no value is passed.

# Example:

def greet(name = "jivika"):  # name has a default value "jivika"
    print("hello",name)
greet()          # uses default argument

# 5. Recursion:
# Recursion is a programming technique where a function calls itself in order to solve a problem.

# Example:

def factorial(n):
    if n == 1:          # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive case
    
# Questions:

# program to print factorial of 5.

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
print("factorial:",fact(5))

# program to print fibonacci series up to n terms.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(10)  # prints first 10 terms of Fibonacci series

# program to check if a number is prime or not.

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
