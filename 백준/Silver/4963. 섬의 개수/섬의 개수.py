# 입력부터 출력까지 직접 작성해 보세요.
import sys
sys.stdin.readline      

while True:
    # width, height 
    m, n = map(int, input().split())
    
    # if 0 0, break loop
    if m == 0 and n == 0 :
        break
    
    def dfs(x, y):
        dir_x = [0, 0, -1, 1, -1, -1, 1, 1]
        dir_y = [1, -1, 0, 0, 1, -1, 1, -1]
        
        stack = [(x, y)]
        visited[y][x] = True
        
        while stack:
            x, y = stack.pop()
            
            for i in range(8):
                dx = x + dir_x[i]
                dy = y + dir_y[i]
                
                if 0 <= dx < m and 0 <= dy < n :
                    if not visited[dy][dx] and map_[dy][dx] == 1:
                        visited[dy][dx] = True
                        stack.append((dx, dy))
    
    map_ = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    answer = 0
    
    for i in range(n):
        for j in range(m):            
            if map_[i][j] == 1 and not visited[i][j]:
                answer += 1
                dfs(j, i)  
                          
    print(answer)           