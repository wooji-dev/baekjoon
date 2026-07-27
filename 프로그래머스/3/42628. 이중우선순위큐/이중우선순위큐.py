import heapq

def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    
    for i in operations:
        order, num = i.split(" ")[0], i.split(" ")[1]
        num = int(num)
        
        if order == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif order == "D" and min_heap:
            if num == 1:
                max_num = heapq.heappop(max_heap)
                min_heap.remove(-max_num)
            elif num == -1:
                min_num = heapq.heappop(min_heap)
                max_heap.remove(-min_num)
        
    if len(min_heap) == 0:
            answer = [0,0]
    else:
        answer = [-heapq.heappop(max_heap), heapq.heappop(min_heap)]    
    return answer