# https://programmers.co.kr/learn/courses/30/lessons/42840

import math

def solution(answers):
    patterns = [[1, 2, 3, 4, 5],
                [2, 1, 2, 3, 2, 4, 2, 5],
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = [0] * len(patterns)
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == (i % 5) + 1:
            score[0] = score[0] + 1
        
        if answers[i] == patterns[1][i % 8]:
            score[1] = score[1] + 1
            
        if answers[i] == patterns[2][i % 10]:
            score[2] = score[2] + 1
            
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i + 1)
            
    return answer
