# https://programmers.co.kr/learn/courses/30/lessons/42895

N, number = map(int, input().split())
values_by_used_cnt = [set([]) * 8]

def BFS(N, used_cnt):
    idx = used_cnt - 1
    
    if idx < 0 or idx > 7:
        return
    if len(values_by_used_cnt[idx]) != 0:
        return
    elif idx == 0:
        print(values_by_used_cnt[0])
        print(values_by_used_cnt[1])
        print(values_by_used_cnt[2])
        values_by_used_cnt[idx].add(N)
        print(values_by_used_cnt[0])
        print(values_by_used_cnt[1])
        print(values_by_used_cnt[2])
        return
    
    BFS(N, idx)
    values_by_used_cnt[idx].add(N * 11)
    
    for i in range(0, used_cnt):
        for val_1 in values_by_used_cnt[i]:
            for val_2 in values_by_used_cnt[idx - i]:
                values_by_used_cnt[idx].add(val_1 + val_2)
                values_by_used_cnt[idx].add(val_1 - val_2)
                values_by_used_cnt[idx].add(val_1 * val_2)
                values_by_used_cnt[idx].add(val_1 / val_2)

for i in range(1, 9):
    BFS(N, i)
    
    if number in values_by_used_cnt[i - 1]:
        print(i)
        break
print(-1)
