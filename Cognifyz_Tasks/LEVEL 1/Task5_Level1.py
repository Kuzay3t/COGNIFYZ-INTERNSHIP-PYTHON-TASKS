# Palindrome Checker
# This is the code for task 5
# This code is for task 1 which is to create a string reverse function and check if it is a palindrome


final_string = "" # defining a global variable to store the reversed string
string = input("Enter a string: ") # taking input from the user


def reverse_string(string):
    '''This function  reverses the string passed to it and checks if it is a palindrome'''
    n = len(string)
    new_string = ""
    for i in range(n): # iterating through the string in reverse order
        new_string += string[n - i - 1]
    final_string = new_string
if final_string == string: # checking if the reversed string is equal to the original string
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

reverse_string(string)