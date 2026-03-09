# 선수 과목 연결 리스트
# 

import sys
from collections import deque

lectures, num = map(int, sys.stdin.readline().split())
rule = [ [] for _ in range(lectures + 1) ]
solution = [0] * (lectures+1)
semester = [0] * (lectures+1)

for i in range(num):
	A, B = map(int, sys.stdin.readline().split())
	rule[A].append(B)
	solution[B] += 1

# 진입 차수가 0인 과목들을 큐에 삽입
queue = deque()
for i in range(1, lectures + 1):
    if solution[i] == 0:
        queue.append(i)
        semester[i] = 1  # 선수 과목이 없으므로 1학기에 수강

while queue:
	cur = queue.popleft()
    
	for i in rule[cur]:
		solution[i] -= 1
		if solution[i] == 0:
			semester[i] = semester[cur] + 1
			queue.append(i)


print(*(semester[1:]))