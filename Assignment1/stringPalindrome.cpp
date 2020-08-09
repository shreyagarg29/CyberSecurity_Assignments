//Write a C/C++ program to check whether a string is palindrome or not.
#include<iostream>
#include<cstring>
using namespace std;
bool checkPalindrome(char str[])
{
    int len = strlen(str);
    int start = 0; 
    int end = len - 1;
    while(start <= end)
    {
        if(str[start] != str[end])
        {
            return false;
        }
        start++;
        end--;
    }
    return true;
}
int main(){
    char str[100];
    cout << "Enter a String : ";
    cin.getline(str,100);
    if(checkPalindrome(str))
    {
        cout << "The given string is PALINDROME" << endl;
    }
    else
    {
        cout << "The given string is NOT PALINDROME" << endl;
    }
}