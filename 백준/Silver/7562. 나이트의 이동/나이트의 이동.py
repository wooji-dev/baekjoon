import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
direction = [
    [-2, 1], [-2, -1], [2, 1], [2, -1],
    [1, -2], [-1, -2], [1, 2], [-1, 2]
]

for _ in range(num):
    width = int(input())

    start = list(map(int, input().split()))
    target = list(map(int, input().split()))

    visited = [[False] * width for _ in range(width)]
    answer = -1

    dq = deque([[start[0], start[1], 0]])
    visited[start[1]][start[0]] = True

    while dq:
        cur_x, cur_y, count = dq.popleft()

        if [cur_x, cur_y] == target:
            answer = count
            break

        for move_x, move_y in direction:
            dx = cur_x + move_x
            dy = cur_y + move_y

            if 0 <= dx < width and 0 <= dy < width:
                if not visited[dy][dx]:
                    visited[dy][dx] = True
                    dq.append([dx, dy, count + 1])

    print(answer)