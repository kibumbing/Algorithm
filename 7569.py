import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

tomato = []
ripe = deque()
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if temp[j][k] == 1:
                ripe.append((i, j, k))
    tomato.append(temp)

rx = [1, -1, 0, 0, 0, 0]
ry = [0, 0, 1, -1, 0, 0]
rz = [0, 0, 0, 0, 1, -1]
while ripe:
    x, y, z = ripe.popleft()
    for j in range(6):
        nx = x + rx[j]
        ny = y + ry[j]
        nz = z + rz[j]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomato[nx][ny][nz] == 0:
            ripe.append((nx, ny, nz))
            tomato[nx][ny][nz] = tomato[x][y][z] + 1

ans = 0
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
            ans = max(ans, k)
print(ans - 1)
