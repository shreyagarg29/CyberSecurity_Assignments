#Write a program to print N fibonacci numbers where N is being passed from command line and you
#can run python program using command - python fibo.py 20, where N=20.
def printFibonacci(n): 
    f1 = 0
    f2 = 1
    if (n < 1): 
        return
    for x in range(0, n): 
        print(f2, end = " ") 
        next = f1 + f2 
        f1 = f2 
        f2 = next
print("Series: ")
print(printFibonacci(20))