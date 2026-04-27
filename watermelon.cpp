
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
using namespace std ;



void isDiv(int value){
    int first_half = value-1;
    int second_half = 1;

    while(first_half > second_half){

        // cout << first_half << endl ;
        // cout << second_half << endl;

        if((first_half % 2) && (second_half % 2)){
             cout << "Yes";
             return;
        }
    
        else{
            first_half-=1;
            second_half +=1;
        }
    }

    cout << "No";
}


int main(){
    int n;
    cin >> n;
    isDiv(n);
    return 0;
}