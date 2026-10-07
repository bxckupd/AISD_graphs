import sys

input = sys.stdin.readline
n = int(input())
names = {}

for _ in range(n):
    name = input().strip()
    if name not in names:
        print("OK")
        names[name] = 1
    else:
        print(name + str(names[name]))
        names[name] += 1
