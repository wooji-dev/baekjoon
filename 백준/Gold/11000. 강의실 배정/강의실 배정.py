import sys
import heapq

# 1. 입력 받기
n = int(sys.stdin.readline().strip())
classroom = []
for _ in range(n):
    classroom.append(list(map(int, sys.stdin.readline().split())))

# 2. 시작 시간 기준으로 정렬
classroom.sort()

# 3. 우선순위 큐(Heap) 생성 - 강의실의 '종료 시간'을 저장함
heap = []
# 첫 번째 수업의 종료 시간을 먼저 넣음
heapq.heappush(heap, classroom[0][1])

for i in range(1, n):
    # 만약 현재 수업의 시작 시간이 가장 빨리 끝나는 방의 종료 시간보다 크거나 같다면
    if classroom[i][0] >= heap[0]:
        # 해당 강의실을 이어서 쓸 수 있으므로 기존 종료 시간을 비움
        heapq.heappop(heap)

    # 새로운 수업의 종료 시간을 힙에 넣음
    # (비워진 자리에 들어가거나, 혹은 새 강의실이 추가되는 효과)
    heapq.heappush(heap, classroom[i][1])

# 힙에 남아있는 원소의 개수가 곧 필요한 최소 강의실 개수임
print(len(heap))