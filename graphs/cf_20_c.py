import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))
dist = [float("inf")] * (n + 1)
parent = [-1] * (n + 1)
dist[1] = 0
heap = [(0, 1)]
while heap:
    d, v = heappop(heap)
    if d != dist[v]:
        continue
    if v == n:
        break
    for u, w in graph[v]:
        new_dist = d + w
        if new_dist < dist[u]:
            dist[u] = new_dist
            parent[u] = v
            heappush(heap, (new_dist, u))
if dist[n] == float("inf"):
    print(-1)
else:
    path = []
    v = n
    while v != -1:
        path.append(v)
        v = parent[v]
    print(*path[::-1])
