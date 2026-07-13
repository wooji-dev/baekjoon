def solution(arr):
    answer = []
    
    prev = arr[0]
    answer.append(prev)
    
    for idx, ele in enumerate(arr, start=1):
        if prev != ele:
            answer.append(ele)
        
        prev = ele
    
    return answer