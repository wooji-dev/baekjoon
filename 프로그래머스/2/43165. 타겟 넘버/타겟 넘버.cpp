#include <string>
#include <vector>

using namespace std;

int answer = 0;

void dfs(const vector<int>& numbers, int target, int idx, int cur_num) {
    if (idx == numbers.size()) {      // 모든 숫자를 다 쓴 뒤에 비교
        if (cur_num == target) answer++;
        return;
    }
    dfs(numbers, target, idx + 1, cur_num + numbers[idx]);
    dfs(numbers, target, idx + 1, cur_num - numbers[idx]);
}

int solution(vector<int> numbers, int target) {
    answer = 0;
    dfs(numbers, target, 0, 0);
    return answer;
}