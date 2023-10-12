import sys
from collections import deque

gear = [deque(sys.stdin.readline().rstrip()) for _ in range(4)]
k = int(sys.stdin.readline())

for _ in range(k):
    num, direct = map(int, sys.stdin.readline().split())

    state = []
    for i in range(4):
        state.append((gear[i][2], gear[i][6]))

    if direct == 1:
        gear[num - 1].rotate(1)
    else:
        gear[num - 1].rotate(-1)

    temp_num = num - 1
    temp_direct = direct
    while temp_num > 0:
        temp_direct *= -1
        if state[temp_num - 1][0] != state[temp_num][1]:
            if temp_direct == 1:
                gear[temp_num - 1].rotate(1)
            else:
                gear[temp_num - 1].rotate(-1)
            temp_num -= 1
        else:
            break

    temp_num = num + 1
    temp_direct = direct
    while temp_num < 5:
        temp_direct *= -1
        if state[temp_num - 1][1] != state[temp_num - 2][0]:
            if temp_direct == 1:
                gear[temp_num - 1].rotate(1)
            else:
                gear[temp_num - 1].rotate(-1)
            temp_num += 1
        else:
            break

score = 0
for i in range(4):
    if gear[i][0] == '1':
        score += 2 ** i
print(score)