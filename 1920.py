import sys

n = int(sys.stdin.readline())
a = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

answer = []
for i in b:
    if i in a:
        answer.append('1')
    else:
        answer.append('0')
print('\n'.join(answer))