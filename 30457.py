import sys

n = int(sys.stdin.readline())
a = tuple(map(int, sys.stdin.readline().split()))

dic = {}
cnt = 0
for i in a:
    if i not in dic:
        dic[i] = 1
    elif dic[i] == 2:
        cnt += 1
    else:
        dic[i] += 1
print(n - cnt)
