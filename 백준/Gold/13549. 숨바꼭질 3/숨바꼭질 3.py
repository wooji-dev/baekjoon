import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

MAX = 100001
dist = [-1] * MAX

def solve():
    queue = deque([N])
    dist[N] = 0 # 시작점은 0초
    
    while queue:
        cur = queue.popleft()
        
        if cur == K:
            return dist[cur]
            
        # 1. 순간이동 (0초 소요) - 가장 먼저 고려되어야 함
        if 0 <= cur * 2 < MAX and dist[cur * 2] == -1:
            dist[cur * 2] = dist[cur]
            queue.appendleft(cur * 2) 
            
        # 2. 걷기 (1초 소요)
        for next_pos in (cur - 1, cur + 1):
            if 0 <= next_pos < MAX and dist[next_pos] == -1:
                dist[next_pos] = dist[cur] + 1
                queue.append(next_pos)

print(solve())