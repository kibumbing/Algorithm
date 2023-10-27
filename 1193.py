import sys

x = int(sys.stdin.readline())
sum = 0
count = 1
while True:
    sum += count
    if sum >= x:
        if count % 2 == 1:
            up = sum - x + 1
            down = count - sum + x
        else:
            up = count - sum + x
            down = sum - x + 1
        break
    count += 1
print(f'{up}/{down}')