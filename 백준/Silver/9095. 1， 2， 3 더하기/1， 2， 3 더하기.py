import sys
from collections import Counter

tests = int(sys.stdin.readline().strip())

def find_exp(num) :
    dp = [[0]]
    answer = 0

    while True:
        prev = len(dp)-1
        cur = [ ]

        for i in dp[prev]:
            for j in range(1, 4):
                cur.append(i + j)

        if cur[0] > num:
            return answer

        if num in cur:
            answer += dict(Counter(cur))[num]
        dp.append(cur)


for test in range(tests):
    test_num = int(sys.stdin.readline().strip())
    print(find_exp(test_num))