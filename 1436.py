import sys

n = int(sys.stdin.readline())
num = 666
idx = 0
while True:
    if '666' in str(num):
        idx += 1
        if idx == n:
            break
    num += 1
print(num)