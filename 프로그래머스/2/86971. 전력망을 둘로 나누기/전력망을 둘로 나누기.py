def solution(n, wires):
    answer = -1
    map = [[] for _ in range(n+1)]
    
    result = n
    
    for i in wires:
        map[i[0]].append(i[1])
        map[i[1]].append(i[0])
        
    def dfs(node, parent):
        nonlocal result
        size = 1
        
        for i in map[node]:
            if i == parent:
                continue
            
            children_size = dfs(i, node)
            
            result = min(result, abs(n - 2*children_size))
            size += children_size
        
        return size
    
    dfs(1,0)
    answer = result
    return answer