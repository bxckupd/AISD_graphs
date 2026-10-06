n = int(input())
graph = [[] for _ in range(n + 1)]
stack = []
for v in range(1, n + 1):
    p = int(input())
    if p == -1:
        stack.append((v, 1))
    else:
        graph[p].append(v)
answer = 0
while stack:
    v, depth = stack.pop()
    answer = max(answer, depth)
    for u in graph[v]:
        stack.append((u, depth + 1))
print(answer)
