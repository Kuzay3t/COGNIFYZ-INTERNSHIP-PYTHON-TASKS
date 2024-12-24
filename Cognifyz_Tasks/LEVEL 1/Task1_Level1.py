# String Reversal

# This code is written for task 1 of level 1
# I am expected to create a string reverse function

string = input("What's the word that you want to reverse? ")

def reverse_string(string):
    """ This function reverses the string passed as a parameter """
    n = len(string)
    new_string = ""
    for i in range(n): # iterating through the string in reverse order
        new_string += string[n - i - 1]
    print(f"The reversed string is {new_string}")

reverse_string(string)
