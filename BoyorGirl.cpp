
#include<string.h>
#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<unordered_set>
using namespace std;

void boy_or_girl(string str){
    unordered_set<char> hashTable;
    
    for(int i=0; i < str.length(); i++){
        hashTable.insert(str[i]);
    }

    if(hashTable.size()%2 == 0){
        cout << "CHAT WITH HER!"<< endl;
    }

    else{
        cout << "IGNORE HIM!" << endl;
    }
    

}



int main(){
    string str;
    cin >> str;

    boy_or_girl(str);

}