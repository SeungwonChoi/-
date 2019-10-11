# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    
    for num_short, num_long in zip(phone_book, phone_book[1:]):
        if num_long.startswith(num_short):
            return False
    return True
