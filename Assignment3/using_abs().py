# Given an integer n, return True if n is within 10 of either 100 or 200
def near_num(num):
    if abs(100 - num) <= 10 or abs(200 - num) <= 10:
        return True
    else:
        return False
num = int(input("Enter the number: "))
print(near_num(num))