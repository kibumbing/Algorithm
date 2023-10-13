# import sys
#
# m, n = map(int, sys.stdin.readline().split())
# arr = [0 for _ in range(n + 1)]
# arr[1] = 1
#
# for i in range(2, n + 1):
#     if arr[i] == 0:
#         arr[i] = 0
#         temp = i + i
#         while temp < n + 1:
#             arr[temp] = 1
#             temp = temp + i
# ans = ''
# for i in range(m, n + 1):
#     if arr[i] == 0:
#         ans = ans + str(i) + '\n'
# print(ans)

# import sys
#
# m, n = map(int, sys.stdin.readline().split())
#
# for i in range(m, n + 1):
#     if i == 1:
#         continue
#     for j in range(2, int(i ** 0.5) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# import sys
#
# m, n = map(int, sys.stdin.readline().split())
# prime = [1] * (n + 1)
# prime[1] = 0
#
# for i in range(2, int(n ** 0.5) + 1):
#     if prime[i]:
#         prime[i * i : n + 1 : i] = [0] * len(range(i * i, n + 1, i))
#
# ans = ''
# for i in range(m, n + 1):
#     if prime[i]:
#         ans = ans + str(i) + '\n'
# print(ans)

import sys

m, n = map(int, sys.stdin.readline().split())
prime = [False, False] + [True] * (n - 1)
for i in range(2, int(n ** 0.5) + 1):
    if prime[i]:
        prime[i * i : n + 1 : i] = [False] * len(range(i * i, n + 1, i))

ans = []
for i in range(m, n + 1):
    if prime[i]:
        ans.append(str(i))
print('\n'.join(ans))