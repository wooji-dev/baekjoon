def solution(clothes):
    answer = 1
    dic = {}
    
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    
    
    for k in dic:
        answer *= dic[k] + 1
    
    return answer - 1