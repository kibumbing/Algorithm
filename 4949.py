import sys
from collections import deque

ans = []
while True:
    sentence = sys.stdin.readline().rstrip()

    if sentence == '.':
        break

    bal = 1
    stack = deque()
    for alpha in sentence:
        if alpha == '(' or alpha == '[':
            stack.append(alpha)
        elif alpha == ')':
            if len(stack) > 0 and stack.pop() == '(':
                continue
            else:
                bal = 0
                break
        elif alpha == ']' :
            if len(stack) > 0 and stack.pop() == '[':
                continue
            else:
                bal= 0
                break
    if len(stack) != 0:
        bal = 0

    if bal == 1:
        ans.append('yes')
    else:
        ans.append('no')
print('\n'.join(ans))