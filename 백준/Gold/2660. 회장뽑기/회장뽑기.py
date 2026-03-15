import sys
from collections import deque

num = int(sys.stdin.readline().strip())
rule = [ [] for _ in range(num+1) ]
score = [0] * (num+1)

while True:
    a, b = map(int, sys.stdin.readline().strip().split())
    if a == -1 and b == -1:
        break
    rule[a].append(b)
    rule[b].append(a)

# 추천하는 각 유저별 점수 계산 로직 (수도코드)
for i in range(1, num + 1):
    # -1로 초기화하면 방문하지 않은 상태를 의미함
    dist = [-1] * (num + 1)  # i번 유저로부터의 거리를 저장할 리스트
    queue = deque([i])
    dist[i] = 0

    while queue:
        curr = queue.popleft()
        for neighbor in rule[curr]:
            if dist[neighbor] == -1:  # 아직 방문 안 했다면
                dist[neighbor] = dist[curr] + 1
                queue.append(neighbor)

    # i번 유저의 점수는 dist 리스트에 저장된 값들 중 최대값!
    score[i] = max(dist[1:])

min_val = min(score[1:])
candidates = [i for i, s in enumerate(score) if i > 0 and s == min_val]

print(f"{min_val} {len(candidates)}")
print(*(candidates))