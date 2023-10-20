import sys

paper = set()

n = int(sys.stdin.readline())

for _ in range(n):
    width, height = map(int, sys.stdin.readline().split())
    for w in range(width, width + 10):
        for h in range(height, height + 10):
            paper.add((w, h))

print(len(paper))