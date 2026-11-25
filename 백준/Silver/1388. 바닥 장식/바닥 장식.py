# 입력부터 출력까지 직접 작성해 보세요.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
map = []

        
def dfs(visited, x, y):
    visited[y][x] = True
    cur = map[y][x]
    
    if cur == '-':
        for dir in [-1,1]:
            dx = x + dir
            if dx > -1 and dx < m and not visited[y][dx] and map[y][dx] == cur:
                dfs(visited, dx, y)
    elif cur == '|':
        for dir in [-1,1]:
            dy = y + dir
            if dy > -1 and dy < n and not visited[dy][x] and map[dy][x] == cur:
                dfs(visited, x, dy)
    

for _ in range(n):
    map.append(list(input().strip()))

# dfs?
# 전체를 돌면서 연속되는 판자 찾기
visited = [[False] * m for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        answer += 1  
        visited[i][j] = True
        cur = map[i][j]

        if cur == '-':
            for dir in [-1,1]:
                dx = j + dir
                if dx > -1 and dx < m and not visited[i][dx] and map[i][dx] == cur:
                    dfs(visited, dx, i)
        elif cur == '|':
            for dir in [-1,1]:
                dy = i + dir
                if dy > -1 and dy < n and not visited[dy][j] and map[dy][j] == cur:
                    dfs(visited, j, dy)
                    
print(answer)
