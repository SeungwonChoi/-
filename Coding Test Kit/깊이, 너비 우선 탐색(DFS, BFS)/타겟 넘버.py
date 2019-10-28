# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    length = len(numbers)
    cnt = 0
    
    def DFS(idx):
        if idx < length:
            DFS(idx + 1)
            numbers[idx] *= -1
            DFS(idx + 1)
        elif sum(numbers) == target:
            nonlocal cnt
            cnt += 1

    DFS(0)
    return cnt
