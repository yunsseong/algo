from collections import deque

t = int(input())
q = deque()
cabbage = []
bug_cnt = 0

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

k_set = deque()
k_set.appendleft([0, 0])
cord_set = deque()
cnt = 0

for i in range(2):
    m, n, k = map(int, input().split())
    cabbage = [[0] * m]*n
    for j in range(k):
        a, b = map(int, input().split())
        k_set.append([b, a])

        while k > 0:
            cord_set.appendleft(k_set.pop())
            k-=1

            while len(cord_set) > 0:
                r, c = cord_set.pop()
                for i in range(4):
                    tmp = [r + dr[i], c + dc[i]]
                    if tmp in k_set:
                        cord_set.appendleft(tmp)
                        k_set.remove(tmp)
                        k -= 1
            cnt += 1

print(cnt)







