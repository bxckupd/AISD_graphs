import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cats = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
stack = [(1, 0, 0)]
answer = 0
while stack:
    v, parent, count = stack.pop()
    if cats[v] == 1:
        count += 1
    else:
        count = 0
    if count > m:
        continue
    if v != 1 and len(graph[v]) == 1:
        answer += 1
    for u in graph[v]:
        if u != parent:
            stack.append((u, v, count))
print(answer)
