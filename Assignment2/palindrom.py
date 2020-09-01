# Write a Python function that checks whether a passed in string is palindrome or not.
def isPalindrome(str):
    for i in range(0, int(len(str)/2)):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
str = input("Enter the string: ")
ans = isPalindrome(str)
if ans:
    print("String is PALINDROME")
else:
    print("String is NOT PALINDROME")