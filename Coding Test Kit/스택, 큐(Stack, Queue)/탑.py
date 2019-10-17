# https://programmers.co.kr/learn/courses/30/lessons/42588

def solution(heights):
    answer = [0] * len(heights)
    for i in range(1, len(heights)):
        for j in range(i - 1, -1, -1):
            print(i, j)
            if heights[j] > heights[i]:
                answer[i] = j + 1
                break;
    return answer
