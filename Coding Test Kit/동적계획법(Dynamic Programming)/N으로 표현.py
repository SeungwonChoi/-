# https://programmers.co.kr/learn/courses/30/lessons/42895

N, number = map(int, input().split())
values_by_used_cnt = [[]] * 8

def BFS(N, used_cnt):
    if len(values_by_used_cnt[used_cnt - 1]) != 0:
        return
    if used_cnt == 1:
        values_by_used_cnt[0] = [N]
    else:
        values_by_used_cnt[used_cnt - 1] = []
        #for in 


BFS(N, 2)
print(values_by_used_cnt[1])
