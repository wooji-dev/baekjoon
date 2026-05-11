from collections import deque

def solution(begin, target, words):
    answer = 0
    
    def count_matches(a, b):
        return sum(c1 == c2 for c1, c2 in zip(a, b))
    
    visited = [False] * len(words)
    dq = deque([[begin, 0]])
    
    while(dq):
        [cur, dist] = dq.popleft();
        
        if cur == target:
            return dist
        
        for i in range(len(words)):
            
            if(visited[i] == False and count_matches(cur, words[i]) == len(words[i]) - 1):
                visited[i] = True;
                dist += 1
                dq.append([words[i],dist])
    
    return 0