def solution(sizes):
    answer = 0
    x = 0
    y = 0
    
    for i in sizes:
        x = max(x, max(i))
        y = max(y, min(i))
        
    answer = x * y
    
    return answer