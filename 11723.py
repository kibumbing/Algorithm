import sys

s = set()
m = int(sys.stdin.readline())
all_s = set([str(i) for i in range(1, 21)])
for _ in range(m):
    input = sys.stdin.readline().rstrip().split()

    if input[0] == 'add':
        s.add(input[1])
    elif input[0] == 'remove':
        s.remove(input[1]) if input[1] in s else 0
    elif input[0] == 'check':
        if input[1] in s:
            print(1)
        else:
            print(0)
    elif input[0] == 'toggle':
        s.remove(input[1]) if input[1] in s else s.add(input[1])
    elif input[0] == 'all':
        s = all_s.copy()
    elif input[0] == 'empty':
        s = set()