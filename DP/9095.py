t = int(input())
n = []
dp = [0 for i in range(11)]

for _ in range(t):
    n.append(int(input()))

max_value = max(n)

dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, max_value+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in n:
    print(dp[i])
