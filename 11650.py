import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort()
for i in range(n):
    print(arr[i][0], arr[i][1])