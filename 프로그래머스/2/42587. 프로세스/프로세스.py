from collections import deque
def solution(priorities, location):
    solution = deque(list(enumerate(priorities)))
    answer = 0 

    while solution:
        max_num = max(priorities) 
        cur = solution.popleft()
        
        if cur[1] >= max_num:
            priorities.pop(0)
            answer += 1
            if cur[0] == location:
                return answer  
        else:
            a = priorities.pop(0)
            priorities.append(a)
            solution.append(cur)
                
    return answer
