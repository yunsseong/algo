from collections import deque
import sys

m, n = map(int, input().split())
tomato = []
day = 1

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

cnt = 0
zero_cnt = 0
q = deque()
for i in range(n):
    tomato.append((input().split()))

for i in range(n):
    for j in range(m):
        if tomato[i][j] == "1":
            q.appendleft((i, j))
        if tomato[i][j] == "0":
            zero_cnt += 1

if zero_cnt == 0:
    print(0)
    sys.exit()

day_per_tomato = len(q)
def bfs(a, b):
    global zero_cnt
    if a >= 0 and a < n and b >= 0 and b < m and tomato[a][b] != "1" and tomato[a][b] !="-1":
        tomato[a][b] = "1"
        zero_cnt -= 1
        q.appendleft((a, b))

while len(q) > 0:
    x, y = q.pop()
    cnt += 1

    for i in range(4):
        bfs(x+dx[i], y+dy[i])

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

