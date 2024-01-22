from collections import deque
import sys

m, n, h = map(int, input().split())
tomato = []
day = 1

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

cnt = 0
zero_cnt = 0
q = deque()
tmp = []
for i in range(h):
    for j in range(n):
        tmp.append((input().split()))
    tomato.append(tmp)
    tmp = []

for i in range(h):
    for j in range(n):
        for k in range(m):
            value = tomato[i][j][k]
            if value == "1": q.appendleft((i, j, k))
            if value == "0": zero_cnt += 1

if zero_cnt == 0:
    print(0)
    sys.exit()

day_per_tomato = len(q)


def bfs(a, b, c):
    global zero_cnt
    if a >= 0 and a < h and b >= 0 and b < n and c >= 0 and c < m and tomato[a][b][c] != "1" and tomato[a][b][c] != "-1":
        tomato[a][b][c] = "1"
        zero_cnt -= 1
        q.appendleft((a, b, c))


while len(q) > 0:
    z, y, x = q.pop()
    cnt += 1

    for i in range(len(dx)):
        bfs(z + dz[i], y + dy[i], x + dx[i])

    if zero_cnt == 0:
        break

    if cnt == day_per_tomato:
        day += 1
        cnt = 0
        day_per_tomato = len(q)

if zero_cnt == 0:
    print(day)
else:
    print("-1")
