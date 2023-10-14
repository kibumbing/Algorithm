import sys

n = int(sys.stdin.readline())

seat = [[0] * n for _ in range(n)]
info = [list(map(int, sys.stdin.readline().split())) for _ in range(n * n)]
fri_record = {}

rx = [0, 0, 1, -1]
ry = [1, -1, 0, 0]
for i in range(n * n):
    info_per = info[i]
    fri_record[info_per[0]] = set(info_per[1:])
    can_sit = []
    for x in range(n):
        for y in range(n):
            if seat[x][y] == 0:
                frieds = 0
                empty = 0
                for i in range(4):
                    nx = x + rx[i]
                    ny = y + ry[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] == 0:
                            empty += 1
                        if seat[nx][ny] in info_per[1:]:
                            frieds += 1
                can_sit.append([frieds, empty, x, y])
    can_sit.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    seat[can_sit[0][2]][can_sit[0][3]] = info_per[0]

total_score = 0
for x in range(n):
    for y in range(n):
        frieds = 0
        for i in range(4):
            nx = x + rx[i]
            ny = y + ry[i]
            if 0 <= nx < n and 0 <= ny < n:
                if seat[nx][ny] in fri_record[seat[x][y]]:
                    frieds += 1
        if frieds > 0:
            total_score += 10 ** (frieds - 1)
print(total_score)