def solution(number, k):
    answer = ''
    
    test = list(map(int, number))
    stack = [test[0]]
    
    for i in range(1, len(test)):
        while len(stack)>0 and k>0 and stack[-1] < test[i]:
            stack.pop()
            k -= 1
        stack.append(test[i])
    
    if k > 0:
        stack = stack[:-k]
            
    answer = "".join(list(map(str,stack)))  
    
    return answer