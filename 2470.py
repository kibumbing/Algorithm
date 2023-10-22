import sys

n = int(sys.stdin.readline())
sol = list(map(int, sys.stdin.readline().split()))
sol.sort()

left = 0
right = n - 1
sum = abs(sol[left] + sol[right])
ans = [sol[left], sol[right]]

while left < right:
    if sum == 0:
        break
    temp = abs(sol[left] + sol[right])
    if temp < sum:
        sum = temp
        ans = [sol[left], sol[right]]
    if sol[left] + sol[right] < 0:
        left += 1
    else:
        right -= 1

print(' '.join(map(str, ans)))