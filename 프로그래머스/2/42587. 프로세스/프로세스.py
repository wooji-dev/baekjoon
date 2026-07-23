def solution(priorities, location):
    answer = 0
    q = []
    
    for idx, ele in enumerate(priorities):
        q.append((ele, idx))
    
    priorities.sort(reverse = True)
    
    while q:
        max_num = priorities[0]
        cur = q.pop(0)
        
        if cur[0] == max_num:
            answer += 1
            if cur[1] == location:
                break
            priorities.pop(0)
        else:
            q.append(cur)
            
        
    return answer