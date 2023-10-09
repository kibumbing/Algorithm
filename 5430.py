import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = deque(sys.stdin.readline()[1:-2].split(","))

    if n == 0:
        arr = deque()

    not_error = 1
    r_num = 0
    for rd in p:
        if rd == 'R':
            r_num += 1
        elif rd == 'D':
            if n < 1:
                print("error")
                not_error = 0
                break
            else:
                if r_num % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
                n -= 1
    if r_num % 2 == 1:
        arr.reverse()
    if not_error:
        print('[' + ','.join(arr) + ']')