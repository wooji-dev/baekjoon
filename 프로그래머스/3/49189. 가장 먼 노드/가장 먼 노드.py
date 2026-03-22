from collections import deque

def solution(n, edge):
    # 1. 인접 리스트 생성 (그래프 연결 상태 저장)
    adj = [[] for _ in range(n + 1)]
    for u, v in edge:
        adj[u].append(v)
        adj[v].append(u)

    # 2. 거리 저장 배열 (-1로 초기화, -1은 미방문을 의미)
    distances = [-1] * (n + 1)
    distances[1] = 0  # 시작 노드(1번)의 거리는 0

    # 3. BFS를 위한 큐 생성 및 시작 노드 삽입
    queue = deque([1])

    while queue:
        curr = queue.popleft()

        for neighbor in adj[curr]:
            # 아직 방문하지 않은 노드라면
            if distances[neighbor] == -1:
                # 현재 노드 거리 + 1을 저장
                distances[neighbor] = distances[curr] + 1
                queue.append(neighbor)

    # 4. 가장 먼 거리 찾기
    max_dist = max(distances)

    # 5. 최대 거리를 가진 노드의 개수 세기
    return distances.count(max_dist)