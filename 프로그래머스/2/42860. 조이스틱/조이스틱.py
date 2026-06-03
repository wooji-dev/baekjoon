def solution(name):
    answer = 0
    
    for char_ in name:
        diff = ord(char_) - ord('A')
        answer += min(diff, 26 - diff)
    
    move = len(name) - 1
    
    for i in range(len(name)):
        next_i = i + 1
        
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        
        move = min(
            move,
            i + i + (len(name) - next_i),        
            (len(name) - next_i) + (len(name) - next_i) + i
        )
    
    answer += move
    return answer