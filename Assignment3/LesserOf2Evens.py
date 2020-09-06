# Write a function that returns the lesser of two given numbers if both
# numbers are even, but returns the greater if one or both numbers are odd
def lesserOfTwo(a,b):
    if (a % 2 or b % 2) != 0:
        if a < b:
            return (b)
        else:
            return (a)
    if (a % 2 and b % 2) == 0:
        if a < b:
            return (a)
        else:
            return (b)
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
print(lesserOfTwo(num1,num2))