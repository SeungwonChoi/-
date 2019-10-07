# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i == j:
                continue;
            if phone_book[j].split(phone_book[i])[0] == "":
                return False
    return True
