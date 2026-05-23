#include<string.h>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cctype>

using namespace std;

int compare(string string1, string string2){
    if (string1 == string2){
        return 0;
    }
    if (string1 > string2){
        return 1;
    }

    return -1;

}


int main(void){
    string my_string1;
    string my_string2;

    cin >> my_string1;
    cin >> my_string2;

    transform(my_string1.begin(),my_string1.end(),my_string1.begin(), [](unsigned char c){ return tolower(c); });
    transform(my_string2.begin(),my_string2.end(),my_string2.begin(), [](unsigned char c){ return tolower(c); });

    cout << compare(my_string1,my_string2) << endl;
    
}