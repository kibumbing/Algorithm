import sys

word = sys.stdin.readline().rstrip()
length = len(word)
for i in range(len(word)):
    if word[i] == '=':
        if i > 1 and word[i - 1] == 'z' and word[i - 2] == 'd':
            length -= 2
        else:
            length -= 1
    elif word[i] == '-':
        length -= 1
    elif word[i] == 'j' and i > 0 and word[i - 1] in ['l', 'n']:
        length -= 1
print(length)