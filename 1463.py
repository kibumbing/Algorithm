# import sys
#
# x = int(sys.stdin.readline())
#
# buf = [1000001 for _ in range(x+1)]
# buf[x] = 0
#
# while x:
#     if x % 3 == 0:
#         buf[x // 3] = min(buf[x // 3], buf[x] + 1)
#     if x % 2 == 0:
#         buf[x // 2] = min(buf[x // 2], buf[x] + 1)
#     buf[x - 1] = min(buf[x - 1], buf[x] + 1)
#     x = x - 1
#
# print(buf[1])

import sys

x = int(sys.stdin.readline())
buf = []
buf.append(x)
count = 0
while 1 not in buf:
    for i in range(len(buf)):
        if buf[i] % 3 == 0:
            buf.append(buf[i] // 3)
        if buf[i] % 2 == 0:
            buf.append(buf[i] // 2)
        if buf[i] - 1 > 1:
            buf.append(buf[i] - 1)
    count += 1
    buf = list(set(buf))
print(count)