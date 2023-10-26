import sys

n = sys.stdin.readline().rstrip()
n = [i for i in n]
n.sort(reverse=True)
print(''.join(n))