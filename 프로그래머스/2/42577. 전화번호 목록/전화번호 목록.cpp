#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    sort(phone_book.begin(), phone_book.end());
        
    for (int i = 0; i + 1 < phone_book.size(); i++) {
        if (phone_book[i + 1].compare(0, phone_book[i].size(), phone_book[i]) == 0)
            return false;
    }
    
    return answer;
}