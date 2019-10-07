# https://programmers.co.kr/learn/courses/30/lessons/42576

import collections

def solution(participant, completion):
    counter_diff = collections.Counter(participant) - collections.Counter(completion)
    return list(counter_diff.keys())[0]
