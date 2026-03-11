
import sys
from collections import deque

# 입력 받기
n, bridge_length, max_weight = map(int, sys.stdin.readline().split())
trucks = deque(list(map(int, sys.stdin.readline().split())))

# 다리 상태를 0으로 초기화 (다리 길이만큼)
bridge = deque([0] * bridge_length)
current_weight = 0
time = 0

while bridge:
    time += 1
    # 1. 다리에서 나가는 트럭 처리
    current_weight -= bridge.popleft()

    # 2. 다리에 진입할 트럭이 남아있는 경우
    if trucks:
        # 새 트럭이 올라갈 수 있는지 확인
        if current_weight + trucks[0] <= max_weight:
            truck = trucks.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            # 하중 초과로 못 올라가면 0을 넣어 트럭들을 전진시킴
            bridge.append(0)

print(time)