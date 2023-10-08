import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
r += 1
c += 1
# room = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
room = [[1] * (m + 2) for _ in range(n + 2)]
for i in range(n):
    temp = [1] + list(map(int, sys.stdin.readline().split())) + [1]
    room[i + 1] = temp

count = 0
while 1:
    if room[r][c] == 0:
        room[r][c] = 2
        count += 1
    if room[r - 1][c] != 0 and room[r + 1][c] != 0 and room[r][c - 1] != 0 and room[r][c + 1] != 0:
        if d == 0:
            if room[r + 1][c] != 1:
                r = r + 1
                continue
            else:
                break
        elif d == 1:
            if room[r][c - 1] != 1:
                c = c - 1
                continue
            else:
                break
        elif d == 2:
            if room[r - 1][c] != 1:
                r = r - 1
                continue
            else:
                break
        else:
            if room[r][c + 1] != 1:
                c = c + 1
                continue
            else:
                break
    else:
        for i in range(4):
            new_d = (d + 3 - i) % 4
            if new_d == 0:
                if room[r - 1][c] == 0:
                    d = new_d
                    r = r - 1
                    break
                else:
                    continue
            elif new_d == 1:
                if room[r][c + 1] == 0:
                    d = new_d
                    c = c + 1
                    break
                else:
                    continue
            elif new_d == 2:
                if room[r + 1][c] == 0:
                    d = new_d
                    r = r + 1
                    break
                else:
                    continue
            else:
                if room[r][c - 1] == 0:
                    d = new_d
                    c = c - 1
                    break
                else:
                    continue
print(count)