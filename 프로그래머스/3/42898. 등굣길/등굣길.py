def solution(m, n, puddles):
    answer = 0
    
    map = [ [0] * (m + 1) for _ in range(n + 1) ]
    map[1][1] = 1
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if [x, y] in puddles:
                map[y][x] = 0
            elif not(x==1 and y==1):
                map[y][x] = (map[y-1][x] + map[y][x-1])%1000000007
    
    answer = map[n][m]
    
    return answer