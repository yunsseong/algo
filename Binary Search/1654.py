k, n = map(int, input().split())
lan_cable = []
for _ in range(k):
    lan_cable.append(int(input()))

s = 0
e = 2**31-1

def cal(num):
    tmp = 0
    for i in lan_cable:
        tmp += i // num
    return tmp

while s <= e:
    m = (s+e) // 2
    num_cable = cal(m)
    if num_cable >= n:
        s = m + 1
    else:
        e = m - 1

print(e)