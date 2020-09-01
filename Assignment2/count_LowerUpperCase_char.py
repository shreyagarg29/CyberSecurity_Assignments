# Write a Python function that accepts a string and calculates the number of upper case letters and
# lower case letters. You can use functions .isupper() and .islower().
def checkCase(str):
    count = {"upper" : 0 , "low" : 0}
    for i in str:
        if i.islower():
            count["low"] = count["low"] + 1
        elif i.isupper():
            count["upper"] = count["upper"] + 1
    print("Uppercase are ",count["upper"])
    print("Lowercase are ", count["low"])
str = input("Enter a string: ")
checkCase(str)
