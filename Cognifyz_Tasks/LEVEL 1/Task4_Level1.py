# Calculator Function

# This code is written for task 4 of level 1
# It is used to perform basic mathematical operations on the given values

First_number = int(input("Enter the first number: "))
Second_number = int(input("Enter the second number: "))


print("""
+
-
*
/
""")
operation = input("Enter the operation you choose to perform: ")

def arithemetic_operation(First_number, Second_number):
    '''This function is used to perform basic arithemetic operations according to the user's request'''
    if operation == "+":
        answer = First_number + Second_number
        print(f" {First_number} + {Second_number} = {answer}")
    elif operation == "-":
        answer = First_number - Second_number
        print(f" {First_number} - {Second_number} = {answer}")
    elif operation == "*":
        answer = First_number * Second_number
        print(f" {First_number} * {Second_number} = {answer}")
    elif operation == "/":
        answer = First_number / Second_number
        print(f"{First_number} / {Second_number} = {answer}")
    else:
        print('Invalid Operation')

arithemetic_operation(First_number, Second_number)