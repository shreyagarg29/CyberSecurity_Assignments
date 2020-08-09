/*
Write a C/C++ program to encrypt and decrypt the string using Caesar Cypher Algorithm. While
encrypting the given string, 5 is added to the ASCII value of the characters. Similarly, 
for decrypting the string, 5 is subtracted from the ASCII value of the characters 
to print an original string. 
*/
#include<iostream>
#include<string>
using namespace std;

string encrypt(string text, int s)
{
    string result = "";
    for (int i=0;i<text.length();i++)
    {
        if (isupper(text[i]))
            result += char(int(text[i]+s-65)%26 +65);

        else
            result += char(int(text[i]+s-97)%26 +97);
    }
    return result;
}


int main()
{
    string text;
    cout << "Enter the text : ";
    getline(cin,text);
    int s = 5;
    cout << "Text : " << text;
    cout << "\nCipher: " << encrypt(text, s);
    return 0;
}