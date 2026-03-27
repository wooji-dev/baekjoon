import sys

num = int(sys.stdin.readline().strip())
scores = [0]  # 1-indexed를 위해 앞에 0 추가

for i in range(num):
    scores.append(int(sys.stdin.readline().strip()))

dp = [0] * (num + 1)
dp[1] = scores[1]

if num >= 2:
    dp[2] = scores[1] + scores[2]
if num >= 3:
    dp[3] = max(scores[1] + scores[3], scores[2] + scores[3])

for i in range(4, num + 1):
    dp[i] = max(
        dp[i-3] + scores[i-1] + scores[i],  # i-1 계단 밟고 오는 경우
        dp[i-2] + scores[i]                  # i-1 계단 안 밟고 오는 경우
    )

print(dp[num])