import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    color = [-1] * (n + 1)
    color[1] = 0
    groups = [[1], []]
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for u in graph[v]:
            if color[u] == -1:
                color[u] = 1 - color[v]
                groups[color[u]].append(u)
                queue.append(u)
    answer = min(groups, key=len)
    print(len(answer))
    print(*answer)
