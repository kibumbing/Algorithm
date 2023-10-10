import sys

n = int(sys.stdin.readline())
arr = set()
for _ in range(n):
    arr.add(sys.stdin.readline())

arr = sorted(list(arr))
arr.sort(key=len)

print(''.join(arr))