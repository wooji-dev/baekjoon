
# DFS

import sys
from collections import deque

col, row, minimum = map(int, sys.stdin.readline().strip().split())
road = []

for i in range(col):
	road.append(list(sys.stdin.readline().strip()))

visited = [[False] * row for _ in range(col)]

direction= [[0,1],[0,-1],[1,0],[-1,0]]


def dfs (x, y, num):
	if x == row - 1 and y == 0:
		if num == minimum: 
			return 1
		return 0
	
	count = 0

	for i in direction:
		dx = x + i[0]
		dy = y + i[1]

		if 0 <= dx < row and 0<= dy < col:
			if not road[dy][dx] == 'T' and not visited[dy][dx]:
				visited[dy][dx] = True
				count += dfs(dx, dy, num+1)
				visited[dy][dx] = False

	return count

visited[col-1][0] = True
answer = dfs(0, col-1, 1)

print(answer)