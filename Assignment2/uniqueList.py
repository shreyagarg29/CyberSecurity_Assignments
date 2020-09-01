# Write a Python function that takes a list and returns a new list with unique
# elements of the first list
def uniqueList(list):
    unique_list = []
    for i in list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
list = []
num = int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(0, num): 
    ele = int(input())
    list.append(ele)
print(uniqueList(list))