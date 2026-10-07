import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = {}
    answer = 0

    for i in range(n):
        value = a[i] - i
        answer += count.get(value, 0)
        count[value] = count.get(value, 0) + 1

    print(answer)
