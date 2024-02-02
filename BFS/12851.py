from collections import deque

n, k = list(map(int, input().split()))
rec = []
q = deque()
q.append((n, 0))
v = [0 for _ in range(100001)]

while q:
    x, sec = q.pop()
    if 0 > x or x > 100000: continue
    if x == k:
        rec.append(sec)
        continue
    if v[x] != 0 and v[x] < sec: continue

    v[x] = sec
    if 0 <= x + 1 <= 100000: q.appendleft((x + 1, sec + 1))
    if 0 <= x - 1 <= 100000: q.appendleft((x - 1, sec + 1))
    if 0 <= x * 2 <= 100000: q.appendleft((x * 2, sec + 1))

min_sec = min(rec)
print(min_sec)
print(rec.count(min_sec))



