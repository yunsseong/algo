n = int(input())
m = [0] * n
ans = 0

def checker(x):
    for i in range(x):
        if m[x] == m[i] or abs(m[x] - m[i]) == abs(x - i):
            return False
    return True


def dfs(x):
    global ans
    if x == n:
        ans += 1

    else:
        for i in range(n):
            m[x] = i
            if checker(x):
                dfs(x+1)

dfs(0)
print(ans)
