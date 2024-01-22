p = 1500000
mod = 1000000
n = int(input()) % p

def fibo(n):
    x, y = 0, 1
    for i in range(0, n):
        x, y = y % mod, (x+y) % mod
    return x

print(fibo(n))