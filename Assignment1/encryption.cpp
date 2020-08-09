/*
You are given a string (you need to take it input from user), the task is to encrypt this string
using # and $ symbols, alternatively. While encrypting the message the encrypted format must repeat
the symbol as many times as the letter position in alphabetical order (consider the string as case
insensitive)
*/
#include<iostream>
#include<string>

using namespace std;

void encrypt(string str)
{
    string enc;
    int h = str.length();
    int i,m;
    char l;
    for(i=0;i<h;i++)
    {
        m=0;
        l=toupper(str[i]);
        m = l-64 ;
        if(i%2==0)
        {
            while(m>0)
            {
                enc.append("#");
                m--;
            }
        }
        else
        {
            while(m>0)
            {
                enc.append("$");
                m--;
            }
        }

    }
    cout << enc << "\n";
}

int main()
{
    string str;
    cout << "Text : ";
    getline (cin,str);
    cout << "Output : ";
    encrypt(str);
    return 0;
}