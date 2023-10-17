import sys

n = int(sys.stdin.readline())
total = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    group = []
    temp = ''
    for i in word:
        if temp != i:
            group.append(i)
        temp = i
    if len(group) == len(set(group)):
        total += 1
print(total)