n, m = map(int, input().split())
tree = list(map(int, input().split()))
s = 0
e = 10000000000

def cal(num):
    tmp = 0
    for i in tree:
        if i > num:
            tmp += i - num
    return tmp


while s <= e:
    mid = (s+e) // 2
    if cal(mid) < m:
        e = mid - 1
    else:
        s = mid + 1

print(e)
