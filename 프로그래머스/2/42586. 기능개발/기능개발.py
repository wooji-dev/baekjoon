import math

def solution(progresses, speeds):
    answer = []
    days = [0] * len(progresses) 
        
    for idx, ele in enumerate(progresses):
        days[idx] = math.ceil((100 - ele) / speeds[idx])
    
    dev = 0
    max = days[0]
    
    for i in range(len(days)):
        dev += 1
        if i == len(days) - 1:
            answer.append(dev)
            break
            
        if max < days[i+1]:
            max = days[i+1]
            answer.append(dev)
            dev = 0
            
    print(days)    
    return answer