import sys
from collections import deque

n = int(sys.stdin.readline())

for _ in range(n):
    ps = sys.stdin.readline().rstrip()
    s = deque()

    ans = 0
    for i in ps:
        if i == '(':
            s.appendleft(1)
        elif i == ')':
            if len(s) > 0 and s[0] == 1:
                s.popleft()
            else:
                print("NO")
                ans = 1
                break
    if ans == 0:
        if len(s) != 0:
            print("NO")
        else:
            print("YES")