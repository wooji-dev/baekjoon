def solution(brown, yellow):
    answer = []
    
    for i in range(1,yellow+1):
        y = i
        x = yellow / y
        if yellow % y == 0 and 2*(x+y) + 4 == brown:
            answer = [x + 2, y + 2]
            break
        
    return answer