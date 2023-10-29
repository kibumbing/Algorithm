import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque(i + 1 for i in range(n))

out = []
cnt = 0
while len(q) > 0:
    cnt += 1
    check = q.popleft()
    if cnt % m == 0:
        out.append(check)
    else:
        q.append(check)
print(f"<{', '.join(map(str, out))}>")
