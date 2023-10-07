import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
lines = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lines[a].append(b)
    lines[b].append(a)
lines = [sorted(line) for line in lines]

ans = ''

visited = []
s = deque()
s.append(v)
while(s):
    val = s.pop()
    if val not in visited:
        visited.append(val)
    else:
        continue
    for i in reversed(lines[val]):
        if i not in visited:
            s.append(i)

ans += ' '.join(map(str, visited)) + '\n'

visited = []
q = deque()
q.appendleft(v)
while(q):
    val = q.pop()
    if val not in visited:
        visited.append(val)
    else:
        continue
    for i in lines[val]:
        if i not in visited:
            q.appendleft(i)
ans += ' '.join(map(str, visited))

print(ans)