# https://programmers.co.kr/learn/courses/30/lessons/42840

import math

def solution(answers):
    pattern_2 = [1, 3, 4, 5]
    pattern_3 = [3, 1, 2, 4, 5]
    score = [0] * 3
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == (i % 5) + 1:
            score[0] = score[0] + 1
        
        if i % 2 == 0 and answers[i] == 2:
            score[1] = score[1] + 1
        elif i % 2 != 0 and answers[i] == pattern_2[math.floor((i % 8) / 2)]:
            score[1] = score[1] + 1
            
        if answers[i] == pattern_3[math.floor((i % 10) / 2)]:
            score[2] = score[2] + 1
            
    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i + 1)
            
    return answer
