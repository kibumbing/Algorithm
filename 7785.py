import sys

n = int(sys.stdin.readline())
in_com = set()

for _ in range(n):
    name, state = sys.stdin.readline().split()

    if state == 'enter':
        in_com.add(name)
    else:
        in_com.discard(name)

in_com = list(in_com)
in_com.sort(reverse=True)

print('\n'.join(in_com))
