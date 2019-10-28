# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    length = len(numbers)
    answer = 0
    
    for i in range(0, pow(2, length)):
        expression = 0
        for j in range(0, length):
            sign = format(i, '0' + str(length) + 'b')[j]
            expression += numbers[j] * (1 if sign == '0' else -1)            
        if expression == target:
            answer += 1
        
    return answer
