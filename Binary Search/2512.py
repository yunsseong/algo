import sys

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

def cal(n):
    tmp = 0
    for i in budget:
        if i > n:
            tmp += n
        else:
            tmp += i

    return tmp

low = 0
high = 1000000000

if sum(budget) <= m:
    print(max(budget))
    sys.exit()

while low <= high:
    mid = (low + high) // 2
    if cal(mid) > m:
        high = mid - 1
    else:
        low = mid + 1

print(high)

