# Write a program to reverse a string:
def reverseString(str):
    words = str.split(' ')   #spliting words
    reversed_String = ' '.join(reversed(words))
    return reversed_String
    
str = input("Enter a string: ")
print (reverseString(str))