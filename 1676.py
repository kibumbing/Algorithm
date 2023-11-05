import sys

n = int(sys.stdin.readline())

num = 1
for i in range(1, n + 1):
    num = num * i

cnt = 0
while True:
    if num % 10 == 0:
        num = num // 10
        cnt += 1
    else:
        break
print(cnt)