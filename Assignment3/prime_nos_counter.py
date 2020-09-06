# Write a function that returns the number of prime numbers that exist up to 
# and including a given number.
def PrimeCounter(n1, n2):
    counter = 0
    for n in range (n1, n2 + 1):
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            counter = counter + 1
    return counter
low_num = int(input("Enter lower limit: "))
upper_num = int(input("Enter the limit: "))
print(PrimeCounter(low_num,upper_num))