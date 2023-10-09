import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

q = deque()
q.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
    check = q.popleft()
    if check == k:
        print(visited[check])
        break
    if check <= 50000 and visited[check * 2] == -1:
        visited[check * 2] = visited[check]
        q.appendleft(check * 2)
    if 1 <= check and visited[check - 1] == -1:
        visited[check - 1] = visited[check] + 1
        q.append(check - 1)
    if check <= 99999 and visited[check + 1] == -1:
        visited[check + 1] = visited[check] + 1
        q.append(check + 1)