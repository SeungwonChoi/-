# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    keep_num = [1]  * n
    for idx in lost:
        keep_num[idx - 1] -= 1
    for idx in reserve:
        keep_num[idx - 1] += 1
        
    for i in range(len(keep_num)):
        if keep_num[i] == 0:
            if i + 1 < len(keep_num) and keep_num[i + 1] == 2:
                keep_num[i] += 1
                keep_num[i + 1] -= 1
            elif i - 1 >= 0 and keep_num[i - 1] == 2:
                keep_num[i] += 1
                keep_num[i - 1] -= 1
                
    return len([i for i in keep_num if i != 0])
