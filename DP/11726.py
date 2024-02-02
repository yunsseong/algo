import sys

n = int(input())

if n < 2:
    print(n)
    sys.exit()

dp = [0 for _ in range(n+1)]
dp[1], dp[2] = 1, 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])