import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])
    
    while heap[0] < K :
        if len(heap) < 2:
            answer = -1
            break
        answer += 1
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        new = a + (b*2)
        heapq.heappush(heap, new)
        
    return answer