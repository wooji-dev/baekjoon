import sys
from itertools import combinations

# 입력 받기
N = int(sys.stdin.readline())
adj = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

members = list(range(N))
min_diff = float('inf')

# 1. 전체 인원의 절반을 뽑아 한 팀(start_team)을 구성
for start_team in combinations(members, N // 2):
    # 2. 나머지 인원으로 상대 팀(link_team) 구성
    link_team = list(set(members) - set(start_team))

    start_score = 0
    link_score = 0

    # 3. 각 팀 내에서 2명씩 조합하여 능력치 합산
    for i, j in combinations(start_team, 2):
        start_score += adj[i][j] + adj[j][i]

    for i, j in combinations(link_team, 2):
        link_score += adj[i][j] + adj[j][i]

    # 4. 두 팀의 점수 차이 최솟값 갱신
    min_diff = min(min_diff, abs(start_score - link_score))

    if min_diff == 0:
        break

print(min_diff)