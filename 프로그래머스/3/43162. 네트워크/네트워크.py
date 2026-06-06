def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(idx):  
        visited[idx] = True
        cur = computers[idx]
        
        for i in range(len(cur)):
            if not visited[i] and cur[i] == 1:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer