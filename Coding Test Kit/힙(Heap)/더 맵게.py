# https://programmers.co.kr/learn/courses/30/lessons/42626

import math

def solution(scoville, K):
    cnt = 0

    while min(scoville) < K and len(scoville) >= 2:
        scoville.sort()
        scoville.insert(0, scoville.pop(0) + 2 * scoville.pop(0))
        cnt += 1
        
    return -1 if min(scoville) < K else cnt
