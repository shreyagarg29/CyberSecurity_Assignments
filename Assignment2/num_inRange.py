# Write a function that checks whether a number is in a given range (inclusive of high and low).
def check_range(low,high,num):
    if num in range(low,high + 1):
        print("Number is in range")
    else:
        print("Number is not in range")
low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))
num = int(input("Enter the number to check: "))
check_range(low,high,num)