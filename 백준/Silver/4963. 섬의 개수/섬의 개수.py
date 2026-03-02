import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()

    idx = 0
    while idx < len(input_data):
        w = int(input_data[idx])
        h = int(input_data[idx+1])
        idx += 2
        
        if w == 0 and h == 0:
            break
        
        grid = []
        for _ in range(h):
            grid.append(list(map(int, input_data[idx : idx + w])))
            idx += w
            
        island_count = 0
        visited = [[False] * w for _ in range(h)]
        
        for r in range(h):
            for c in range(w):
                if grid[r][c] == 1 and not visited[r][c]:
                    island_count += 1
                    bfs(r, c, h, w, grid, visited)
        
        print(island_count)

def bfs(r, c, h, w, grid, visited):
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, -1, 1]
    
    queue = deque([(r, c)])
    visited[r][c] = True
    
    while queue:
        curr_r, curr_c = queue.popleft()
        
        for i in range(8):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            
            if 0 <= nr < h and 0 <= nc < w:
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))


solve()