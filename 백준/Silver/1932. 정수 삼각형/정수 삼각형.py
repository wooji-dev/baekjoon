import sys

rows = int(sys.stdin.readline().strip())
nums = [[0]]
for i in range(rows):
    nums.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [[] for _ in range(rows+1)]

dp[0].append(0)
dp[1] = nums[1]

for i in range(2, rows+1):
    for j in range(len(nums[i])):
        if j == 0:
            dp[i].append(dp[i-1][j] + nums[i][j])
        elif j == len(nums[i]) - 1:
            dp[i].append(dp[i - 1][j-1] + nums[i][j])
        else:
            a = max(dp[i-1][j-1] + nums[i][j], dp[i-1][j]+nums[i][j])
            dp[i].append(a)

print(max(dp[rows]))