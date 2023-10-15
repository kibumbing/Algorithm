import sys

n = int(sys.stdin.readline())
member = [tuple(sys.stdin.readline().split()) for i in range(n)]
member.sort(key=lambda x : int(x[0]))
member = [member[i][0] + ' ' + member[i][1] for i in range(n)]
print('\n'.join(member))