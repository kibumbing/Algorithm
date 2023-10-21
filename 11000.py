import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
lectures = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
lectures.sort()
rooms = []

heappush(rooms, lectures[0][1])
for i in range(1, n):
    if rooms[0] <= lectures[i][0]:
        heappop(rooms)
    heappush(rooms, lectures[i][1])
print(len(rooms))