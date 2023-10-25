# import sys
#
# n = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# cards.sort()
# m = int(sys.stdin.readline())
# cards2 = list(map(int, sys.stdin.readline().split()))
#
# def bs(x):
#     low = 0
#     high = n - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if cards[mid] == x:
#             print(1)
#             return
#         elif cards[mid] > x:
#             high = mid - 1
#         else:
#             low = mid + 1
#     print(0)
#
# for i in cards2:
#     bs(i)

import sys

n = sys.stdin.readline()
cards = set(sys.stdin.readline().split())
m = sys.stdin.readline()
cards2 = sys.stdin.readline().split()
print(" ".join("1" if i in cards else "0" for i in cards2))