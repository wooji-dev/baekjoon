#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) { 
    string answer = "";
    unordered_map<string,int> marathon;
    
    for(string name : participant) marathon[name] += 1;
    for (const string& name : completion) marathon[name]--;
    
    for(auto& p : marathon){
        if(p.second > 0) return p.first;
    }
    
    return answer;
}