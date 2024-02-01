from collections import deque
q = deque()
n, m = map(int, input().split())

rel = [[] for i in range(n+1)]
v = [0 for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    rel[a].extend([b])
    rel[b].extend([a])

cnt_list = [0 for _ in range(n+1)]

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        v = [0 for _ in range(n + 1)]
        if i == j: continue
        v[i] = 1
        q.append((rel[i], cnt))

        while q:
            next, cnt = q.pop()
            cnt += 1
            for k in next:
                if v[k] == 1: continue

                v[k] = 1
                if k == j:
                    cnt_list[i] += cnt
                    break
                else:
                    q.appendleft((rel[k], cnt))
        cnt = 0

min_value = min(cnt_list[1:])
print(cnt_list.index(min_value))




