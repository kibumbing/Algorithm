import sys

n = int(sys.stdin.readline())
pos = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
pos.sort(key=lambda x:(x[1], x[0]))

for i in range(n):
    print(' '.join(map(str, pos[i])))