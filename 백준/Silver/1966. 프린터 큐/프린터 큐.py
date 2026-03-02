import sys
from collections import deque

num = int(sys.stdin.readline())

for _ in range(num):
    n, m = map(int, sys.stdin.readline().split())
    
    queue = deque(list(map(int, sys.stdin.readline().split())))
    queue = deque([(v, i) for i, v in enumerate(queue)])
    
    count = 0
    
    while queue:
        current = queue.popleft()
        
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else:
            count += 1
            if current[1] == m:
                print(count)
                break