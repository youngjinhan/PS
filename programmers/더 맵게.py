import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0]<K:
        if len(scoville)<=1:
            return -1
        new=heapq.heappop(scoville)+2*heapq.heappop(scoville)
        heapq.heappush(scoville, new)
        answer+=1
    
    return answer
