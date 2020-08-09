/*
Write a C/C++ program that lists down all the prime numbers 
in a range between a and b, where a and b are two whole numbers.
*/
#include<iostream>
using namespace std;
int checkPrime(int n)
{
    int isprime = 1;
    for(int i = 2; i <= n / 2; i++)
    {
        if(n % i == 0)
        {
            isprime = 0;
            break;
        }

    }
    return isprime;
}
int main(){
    int num1, num2;
    cout << "Enter first positive integer : ";
    cin >> num1;
    cout << "Enter second positive integer : ";
    cin >> num2;

    cout << "Prime numbers between " << num1 << " and " << num2 << " are : ";
    for(int i = num1; i <= num2; i++)
    {
        if(checkPrime(i) == 1)
        {
            cout << i << " ";
        }
    }
    return 0;
}