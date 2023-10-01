import sys

def sol():
    n = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    print('\n'.join(map(str, sorted(arr))))

sol()