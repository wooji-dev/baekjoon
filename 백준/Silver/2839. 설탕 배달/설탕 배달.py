import sys

sugar = int(sys.stdin.readline().strip())
answer = 0
add_num = [3,5]
dp = [[3,5]]

if sugar == 3 or sugar == 5:
    print(1)
else:
    while True:
        prev = len(dp) - 1
        cur = []
        for i in dp[prev]:
            for j in add_num:
                if i+j not in cur:
                    cur.append(i+j)

        dp.append(cur)
        if sugar in cur:
            print(len(dp))
            break

        if cur[0] > sugar:
            print(-1)
            break
