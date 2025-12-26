#include <unordered_map>
#include <vector>
#include <stdlib.h>
#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

vector<int> frequencySort(vector<int> &nums)
{
    unordered_map<int, int> hashmap;
    priority_queue<pair<int,int>> priorityQueue ;
    for(int i=0; i < nums.size(); i++){
        hashmap[nums[i]] += 1;
    }

    for(auto &p : hashmap){
        pair<int,int> temp;
        temp.first = p.second;
        temp.second = -p.first;
        priorityQueue.push(temp);
        cout << p.first << " " << p.second << endl;
    }
    cout <<"-----------------------------------------------------------------------------"<<endl;
    vector<int> result;
    while(!priorityQueue.empty()){
        
        pair<int,int> temp = priorityQueue.top() ; 
        priorityQueue.pop();

        for(int i=0 ; i < temp.first; i++){
            result.push_back(-temp.second);
        }
        cout << temp.first << " " << temp.second << endl;
    }

    reverse(result.begin(),result.end());
    return result;
}


int main(){
    vector<int> unsortedArray = {-1,1,-6,4,5,-6,1,4,1};
    vector<int> sortedArray = frequencySort(unsortedArray);

    for(int i =0; i < sortedArray.size(); i++){
        cout << sortedArray[i] << endl;
    }
    return 0;
}
