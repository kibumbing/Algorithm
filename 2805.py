# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# trees = list(map(int, sys.stdin.readline().split()))
# start = 0
# end = max(trees)
#
# while start <= end:
#     mid = (start + end) // 2
#     sum = 0
#     for tree in trees:
#         if tree > mid:
#             sum += tree - mid
#     if sum < m:
#         end = mid - 1
#     else:
#         start = mid + 1
# print(end)

import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())
trees = Counter(map(int, sys.stdin.readline().split()))
start = 0
end = max(trees)
while start <= end:
    mid = (start + end) // 2
    if sum((tree - mid) * cnt for tree, cnt in trees.items() if tree > mid) < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)