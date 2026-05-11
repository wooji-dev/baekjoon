from collections import deque

def solution(maps):
    answer = 0
    row, col = len(maps[0]), len(maps)
    visited = [[False] * len(maps[0]) for i in range(len(maps))]
    
    
    dq = deque([[0,0,0]])
    visited[0][0] = True;
    
    while(dq):
        [curX, curY, dist] = dq.popleft()
        dist += 1;
        direction = [[0,1],[0,-1],[1,0],[-1,0]]        

        for i in direction:
            dx, dy = curX+i[0], curY+i[1]

            if(dx == row - 1 and dy == col -1):
                return dist + 1

            if(dx >= 0 and dx < row and dy >= 0 and dy < col and maps[dy][dx] == 1 and visited[dy][dx] == False):
                visited[dy][dx] = True
                dq.append([dx, dy, dist])
    
    return -1
    