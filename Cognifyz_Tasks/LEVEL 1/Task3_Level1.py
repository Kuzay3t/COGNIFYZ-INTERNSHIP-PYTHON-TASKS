# Email Validator

# This code is written for task 3 of level 1
# This is a python function that validates an email adress

email_adress = input("Give me your email adress: ")

def email_checker(email_adress):
    '''The function checks if @ and .com is in the given string
    and validates as an email adress or not'''
    if "@" and ".com" in email_adress:
        print("This is a valid email adress")
    else:
        print("This is not a valid email adress")


email_checker(email_adress)