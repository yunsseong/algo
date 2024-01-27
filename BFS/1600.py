from collections import deque

k = int(input())
mc, mr = map(int, input().split())
q = deque()
m = []
dhr = [-2, -2, -1, -1, 1, 1, 2, 2]
dhc = [-1, 1, -2, 2, -2, 2, -1, 1]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for _ in range(mr):
    m.append(list(map(int, input().split())))

v = [[[0 for _ in range(mc)] for _ in range(mr)] for _ in range(k+1)]
cnt_list = []
def bfs(r, c, kv, cnt):
    if 0 <= r < mr and 0 <= c < mc and m[r][c] != 1 and v[kv][r][c] != 1:
        if r == (mr - 1) and c == (mc - 1):
            cnt_list.append(cnt)
            return
        v[kv][r][c] = 1
        if kv < k:
            for i in range(8):
                q.appendleft((r + dhr[i], c + dhc[i], kv + 1, cnt + 1))

        for i in range(4):
            q.appendleft((r + dr[i], c + dc[i], kv, cnt + 1))

q.append((0, 0, 0, 0))
while q:
    r, c, kv, cnt = q.pop()
    bfs(r, c, kv, cnt)

if len(cnt_list):
    print(min(cnt_list))
else:
    print(-1)