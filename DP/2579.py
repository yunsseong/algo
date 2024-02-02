import sys

n = int(input())
stair = []
dp = [0 for _ in range(n)]

for _ in range(n):
    stair.append(int(input()))

if n == 1:
    print(stair[0])
    sys.exit()

if n == 2:
    print(max(stair[1], stair[1] + stair[0]))
    sys.exit()

dp[0] = stair[0]
dp[1] = max(stair[1], stair[1] + stair[0])
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n):
    dp[i] = max(dp[i-2]+stair[i], stair[i-1]+stair[i]+dp[i-3])

print(dp[n-1])