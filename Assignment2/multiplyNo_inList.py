# Write a Python function to multiply all the numbers in a list and return the result.
def multiply(lst):
	product = 1
	for x in lst:
		product *= x

	return product 
lst = []
num = int(input("Enter the number of elements: "))
print("Enter the elements: ")
#adding elements in list
for i in range(0, num): 
    ele = int(input())
    lst.append(ele)
print(multiply(lst))