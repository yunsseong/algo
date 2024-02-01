n, b = map(int, input().split())

m = []
for _ in range(n):
    m.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        m[i][j] = m[i][j] % 1000

def cal(m1, m2):
    r = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r[i][j] += m1[i][k] * m2[k][j]
            r[i][j] = r[i][j] % 1000
    return r

def print_matrix(m):
    for i in m:
        print(' '.join(list(map(str, i))))

def matcal(b):
    if b == 1:
        return m

    t = matcal(b // 2)
    t = cal(t, t)

    if b % 2 != 0:
        t = cal(t, m)
    return t

print_matrix(matcal(b))





