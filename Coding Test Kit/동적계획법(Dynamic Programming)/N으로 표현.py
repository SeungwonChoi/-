# https://programmers.co.kr/learn/courses/30/lessons/42895

values_by_used_cnt = [set([]) for i in range(0, 9)]
def BFS(N, used_cnt):
    idx = used_cnt - 1
    
    if idx < 0 or idx > 7:
        return
    if len(values_by_used_cnt[idx]) != 0:
        return
    
    BFS(N, idx)
    values_by_used_cnt[idx].add(eval(str(N) * used_cnt))
    
    for i in range(0, int(used_cnt / 2)):
        for val_1 in values_by_used_cnt[i]:
            for val_2 in values_by_used_cnt[idx - 1 - i]:
                values_by_used_cnt[idx].add(val_1 + val_2)
                values_by_used_cnt[idx].add(val_1 - val_2)
                values_by_used_cnt[idx].add(val_2 - val_2)
                values_by_used_cnt[idx].add(val_1 * val_2)
                if val_1 != 0: values_by_used_cnt[idx].add(val_2 / val_1)
                if val_2 != 0: values_by_used_cnt[idx].add(val_1 / val_2)

def solution(N, number):
    for i in range(1, 9):
        BFS(N, i)
        if number in values_by_used_cnt[i - 1]:
            return i
        
    return -1
