import sys

t = int(sys.stdin.readline())
dp = [-1 for _ in range(31)]
dp[0] = 1
dp[1] = 1

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    cnt = 1
    while cnt <= m:
        if dp[cnt] == -1:
            dp[cnt] = cnt * dp[cnt - 1]
        cnt += 1

    print(dp[m] // dp[m - n] // dp[n])

