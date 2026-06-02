from collections import Counter
def solution(n, results):
    answer = 0
    
    reachable = [[False] * (n+1) for _ in range(n+1)]
    
    for i in results:
        reachable[i[0]][i[1]] = 'win'
        reachable[i[1]][i[0]] = 'lose'
    
    
    for k in range(1, n + 1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if reachable[i][k] == 'win' and reachable[k][j] == 'win':
                    reachable[i][j] = 'win'
                elif reachable[i][k] == 'lose' and reachable[k][j] == 'lose':
                    reachable[i][j] = 'lose'
    
    for i in reachable:
        counter = Counter(i)
        
        if counter['win'] + counter['lose'] == n-1:
            answer += 1
        
    return answer