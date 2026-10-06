n = int(input())
f = [0] + list(map(int, input().split()))
answer = "NO"
for a in range(1, n + 1):
    b = f[a]
    c = f[b]
    if f[c] == a:
        answer = "YES"
        break
print(answer)
