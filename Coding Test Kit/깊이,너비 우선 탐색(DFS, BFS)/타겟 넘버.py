# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    length = len(numbers)
    answer = 0
    
    for i in range(0, pow(2, length)):
    expression = ''
    for j in range(0, length):
        sign = format(i, '0' + str(length) + 'b')[j]
        expression += '+' if sign == '0' else '-'
        expression += str(numbers[j])
    if eval(expression) == target:
        answer += 1
        
    return answer
