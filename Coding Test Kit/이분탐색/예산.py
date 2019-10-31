# https://programmers.co.kr/learn/courses/30/lessons/43237

import math

def solution(budgets, M):
    mean = M / len(budgets)
    if max(budgets) <= mean:
        return max(budgets)
    elif min(budgets) >= mean:
        return math.floor(mean)
    
    '''
    while():
        lowest = 0
        highest = M
    '''
    gap_sum = sum([mean - i for i in budgets if i < mean])
    return min(math.floor(mean + gap_sum / max([len([i for i in budgets if i > mean]), 1])), max(budgets))
