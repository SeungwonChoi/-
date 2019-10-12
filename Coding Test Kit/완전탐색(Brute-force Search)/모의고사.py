# https://programmers.co.kr/learn/courses/30/lessons/42840

import math

def solution(answers):
    patterns = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0] * len(patterns)
    
    for question_num, answer in enumerate(answers):
        if answer == (question_num % 5) + 1:
            scores[0] = scores[0] + 1
        
        if answer == patterns[1][question_num % 8]:
            scores[1] = scores[1] + 1
            
        if answer == patterns[2][question_num % 10]:
            scores[2] = scores[2] + 1
    
    return [i + 1 for i, score in enumerate(scores) if score == max(scores)]
