# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) >= 2:
        heapq.heappush(scoville, heapq.heappop(scoville) + 2 * heapq.heappop(scoville))
        cnt += 1
    
    return -1 if scoville[0] < K else cnt
