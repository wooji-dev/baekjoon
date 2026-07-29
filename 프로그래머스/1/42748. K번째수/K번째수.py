def solution(array, commands):
    answer = []
    
    for i in commands:
        i,j,k = i
        array_ = array
        array_ = array[(i-1):j]
        array_.sort()
        answer.append(array_[k-1])
    
    return answer