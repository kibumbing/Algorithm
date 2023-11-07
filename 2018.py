# import sys
#
# n = int(sys.stdin.readline())
#
# count = 0
# start = 1
# end = 1
# sum = 0
# while start <= n:
#     while sum < n and end <= n:
#         sum += end
#         end += 1
#     if sum == n:
#         count += 1
#     sum -= start
#     start += 1
# print(count)

import sys

n = int(sys.stdin.readline())

cnt = 0
temp = 1
while True:
    if n % temp == 0:
        cnt += 1
    n -= temp
    temp += 1

    if n <= 0:
        break
print(cnt)