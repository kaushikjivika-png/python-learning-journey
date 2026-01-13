# Python:

# Day 7: Python File Input/Output
# Topics covered: File handling, reading from files, writing to files, file modes, Deleting files

# 1. File Handling in Python

# In Python, file handling is done using built-in functions. You can open, read, write, and close files using these functions.
# The basic syntax to open a file is:
# file = open('filename', 'mode')

# 2. File Modes:
# 'r' - Read mode (default): Opens a file for reading. The file must exist.
# 'w' - Write mode: Opens a file for writing. If the file exists,

# modes of reading:
# 1-f.read()
# 2-f.readline()

# example:

f = open("demo.txt","r")
data = f.read(6)
print(data)
f.close()

# example 2:

f = open("demo.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()

# modes of writing :
# 1-f.write()

# example:

f = open("demo.txt","w")
f.write("i love to listen music")
f.close()

# example 2:

f = open("demo.txt","a")
f.write("\nand walking to counting my steps")
f.close()

# with syntax:

with open("demo.txt","mode")as f:
      data = f.read()

with open("demo.txt","r")as f:
    print(f.read())

with open("demo.txt","w")as f:
    f.write("i am jiya")

# Deleting a file:

# using the os module
# module(like a code libarary) is a file written by another programmer that generallyy has a function we can use.
# syntax of deleting:
# import os
# os.remove(filename)

# example:

import os
os.remove("demo.txt")

