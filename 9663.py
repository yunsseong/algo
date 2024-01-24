from collections import deque

n = int(input())
q = deque()

dr = [-2, -2, -1, -1, 1, 1, 2, 2]
dc = [-1, 1, -2, 2, -2, 2, -1, 1]
cnt = 0
qcnt = 0
def checker(r, c):
    global cnt, qcnt
    q.appendleft((r, c))
    qcnt = 0
    m = [[0 for _ in range(n)] for _ in range(n)]
    while len(q) > 0:
        r, c = q.pop()
        print(r, c)
        for i in range(len(dr)):
            cr, cc = r + dr[i], c + dc[i]

            if 0 <= cr < n and 0 <= cc < n and m[cr][cc] != 1:
                m[cr][cc] = 1
                q.appendleft((cr, cc))
                qcnt += 1


for i in range(n):
    for j in range(n):
        checker(i, j)

print(qcnt)