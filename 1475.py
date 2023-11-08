import sys
import math

n = sys.stdin.readline().rstrip()
dic = {}
for i in range(10):
    dic[str(i)] = 0

for i in n:
    dic[i] += 1

dic['6'] = math.ceil((dic['6'] + dic['9']) / 2)
dic['9'] = 0

print(max(dic.values()))