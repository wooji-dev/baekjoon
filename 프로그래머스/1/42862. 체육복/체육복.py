def solution(n, lost, reserve):
    answer = 0
    lost = set(lost)
    reserve = set(reserve)
    
    common = lost & reserve
    
    lost = lost - common
    reserve = reserve - common
    
    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
    
    answer = n - len(lost)
    return answer