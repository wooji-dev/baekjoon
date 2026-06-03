def solution(k, dungeons):
    answer = -1
    visited = [False] * len(dungeons)
    
    def dfs(hp, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(len(dungeons)):
            [need, use] = dungeons[i]
            
            if not visited[i] and hp >= need:
                visited[i] = True
                dfs(hp-use, cnt+1)
                visited[i] = False
    
    dfs(k,0)
    return answer