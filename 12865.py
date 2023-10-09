# import sys
#
# n, k = map(int, sys.stdin.readline().split())
# w = [0 for _ in range(n)]
# v = [0 for _ in range(n)]
# dp = [0 for _ in range(k+1)]
# check = [[0] * n for _ in range(k+1)]
# for i in range(n):
#     w[i], v[i] = map(int, sys.stdin.readline().split())
#     if v[i] <= k:
#         dp[w[i]] = v[i]
#         check[w[i]][i] = 1
#
# for i in range(k+1):
#     cur_w = i
#     cur_v = dp[i]
#     for j in range(n):
#         if cur_w + w[j] <= k and check[cur_w][j] == 0 and cur_v + v[j] > dp[cur_w + w[j]]:
#             dp[cur_w + w[j]] = cur_v + v[j]
#             check[cur_w + w[j]] = check[cur_w].copy()
#             check[cur_w + w[j]][j] = 1
#
# print(max(dp))

import sys

n, k = map(int, sys.stdin.readline().split())
wv = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
wv.sort()
dp = [0 for _ in range(k+1)]

for w, v in wv:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i - w] + v, dp[i])

print(max(dp))

