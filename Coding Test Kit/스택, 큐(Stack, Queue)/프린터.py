# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque
def solution(priorities, location):
    cnt = 0
    queue = deque(priorities)
    while(True):
        if queue[0] != max(queue):
            queue.append(queue.popleft())
            location = len(queue) - 1 if location == 0 else location - 1
        else:
            queue.popleft()
            cnt += 1
            location -= 1
        if location == -1:
            return cnt
