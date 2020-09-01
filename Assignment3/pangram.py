# Write a Python function to check whether a string is pangram or not.
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
str = input("Enter a string: ")
if(ispangram(str) == True): 
    print("String is a PANGRAM") 
else: 
    print("String is NOT PANGRAM") 