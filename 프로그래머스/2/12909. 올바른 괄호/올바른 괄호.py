def solution(s):
    answer = True
    items = []
    s = list(s)
        
    for idx, ele in enumerate(s):
        if ele == ")":
            if len(items) > 0:
                if items.pop() != "(":
                    items.append(ele)                    
            else:
                items.append(ele)  
        else:
            items.append(ele)    
            
    if len(items) > 0:
        answer = False
    
    return answer