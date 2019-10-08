# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands:
        start, end, position = command
        answer.append(sorted(array[start - 1:end])[position - 1])
    return answer
