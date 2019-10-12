# https://programmers.co.kr/learn/courses/30/lessons/42840

import math

def solution(answers):
    patterns = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0] * len(patterns)
    
    for question_num, answer in enumerate(answers):
        for i, pattern in enumerate(patterns):
            if answer == pattern[question_num % len(pattern)]:
                scores[i] += 1
    
    return [i + 1 for i, score in enumerate(scores) if score == max(scores)]
