# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    cnt = 0

    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < K and len(heap) >= 2:
        heapq.heappush(heap, heapq.heappop(heap) + 2 * heapq.heappop(heap))
        cnt += 1

    return -1 if heap[0] < K else cnt
