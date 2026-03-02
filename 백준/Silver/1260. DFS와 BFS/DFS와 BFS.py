import sys
from collections import deque


num, lines, start = map(int, sys.stdin.readline().strip().split())
arr = [ [] for _ in range(num+1) ]

for _ in range(lines):
	a, b = map(int, sys.stdin.readline().strip().split())
	arr[a].append(b)
	arr[b].append(a)

for i in range(1, num + 1):
    arr[i].sort()

dfs_visited = [False] * (num+1)
dfs_solution = []

bfs_visited = [False] * (num+1)
bfs_solution = []

def dfs(start):
	dfs_visited[start] = True
	dfs_solution.append(start)

	for i in arr[start]:
		if not dfs_visited[i]:
			dfs(i)



def bfs(start):
	bfs_visited[start] = True
	queue = deque([start])

	while queue:
		point = queue.popleft()
		bfs_solution.append(point)
		for i in arr[point]:
			if not bfs_visited[i]:
				bfs_visited[i] = True
				queue.append(i)


dfs(start)
bfs(start)
print(*dfs_solution)
print(*bfs_solution)