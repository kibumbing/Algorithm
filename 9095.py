import sys

case = int(sys.stdin.readline())
dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(case):
    n = int(sys.stdin.readline())

    for i in range(4, n + 1):
        if dp[i] == 0:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n])