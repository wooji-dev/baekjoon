import sys

num = int(sys.stdin.readline().strip())
dp = [[num]]

if num == 1:
    print(0)
else:
    while True:
        prev = len(dp) - 1
        cur = []

        for i in dp[prev]:
            if i%3 == 0:
                cur.append(i/3)
            if i%2 == 0:
                cur.append(i/2)

            cur.append(i-1)

        if 1 in cur:
            print(len(dp))
            break
        dp.append(cur)