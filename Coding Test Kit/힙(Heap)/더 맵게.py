# https://programmers.co.kr/learn/courses/30/lessons/42626

import math

def solution(scoville, K):
    scoville = [i for i in scoville if i < K]
    answer = math.ceil(math.log(len(scoville)))
    return answer
