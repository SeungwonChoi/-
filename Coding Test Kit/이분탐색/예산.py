# https://programmers.co.kr/learn/courses/30/lessons/43237

import math

def solution(budgets, M):
    mean = M / len(budgets)
    gap_sum = sum([mean - i for i in budgets if i < mean])
    return math.floor(mean + gap_sum / len([i for i in budgets if i > mean]))
