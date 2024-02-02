n = int(input())
a = list(map(int, input().split()))
d = [1 for _ in range(n+1)]

for i in range(1, n):
    for j in range(i):
        if a[j] > a[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))