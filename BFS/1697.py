import sys
from collections import deque

n, k = map(int, input().split())
q = deque()
t = 0
q.appendleft([n, 0])
check = [0 for _ in range(100001)]

def bfs(num, time):
    if 0 <= num <= 100000 and check[num] != 1:
        check[num] = 1
        q.appendleft([num, time])


while len(q) > 0:
    subin_loc, time = q.pop()

    if subin_loc == k:
        print(time)
        sys.exit()

    bfs(subin_loc + 1, time + 1)
    bfs(subin_loc - 1, time + 1)
    bfs(subin_loc * 2, time + 1)
