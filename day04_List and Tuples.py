# Python:

# Day 4: Python List and Tuples
# Topics covered: list, List slicing, List Functions, Tuple, Tuple slicing, Tuple Function, practice Questions.

# 1. List:

names = ["riya","pooja","jiya"]
print(names)

# 2. List slicing:

names = ["sona","shikha","seema"]
print(names[0:2])

# 3. List Functions:

"""1-list.append(). #adds elements in the list.
   2-list.sort(). #sorting the list in ascending order.
   3-list.sort(reverse=True). #sort the list in descending order.
   4-list.reverse(). #reverse the list.
   5-list.insert("old","new"). #insert element at a particular index.
   6-list.remove(el). #remive the element from the list.
   7-list.pop(). #pop out the random value from the list."""

# 4. Tuple:

tuple = (1,2,3,5,6)
print(type(tuple))

# 5. Tuple slicing:

number = (1,2,3,4)
print(number[1:3])

# 6. Tuple function:

"""1-tup.index(El). #finds out the index no.of the element in a tuple.
   2-tup.count(el). #find the occurance of the element in a tuple."""

# Practice questions:

# program to take input from user and print a movie list.

movies = []
mov1 = input("enter first movie:")
mov2 = input("enter second movie:")
mov3 = input("enter third movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

# program to check if a list is palindrome or not.

list = [1,2,3,2,1]
copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
    print("palindrome")
else:
    print("non palindrome")

# program to count how many A are in a list.

grade = ["A","B","C","A","F","A","C","E"]
print(grade.count("A"))




