import sys

input = sys.stdin.readline
MOD1 = 10 ** 9 + 7
MOD2 = 10 ** 9 + 9
BASE = 31
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    power1 = [1] * (n + 1)
    power2 = [1] * (n + 1)
    hash1 = [0] * (n + 1)
    hash2 = [0] * (n + 1)

    for i in range(n):
        value = ord(s[i]) - ord("a") + 1
        power1[i + 1] = power1[i] * BASE % MOD1
        power2[i + 1] = power2[i] * BASE % MOD2
        hash1[i + 1] = (hash1[i] * BASE + value) % MOD1
        hash2[i + 1] = (hash2[i] * BASE + value) % MOD2

    hashes = set()

    for i in range(n - 1):
        right_length = n - i - 2
        right1 = (hash1[n] - hash1[i + 2] * power1[right_length]) % MOD1
        right2 = (hash2[n] - hash2[i + 2] * power2[right_length]) % MOD2
        result1 = (hash1[i] * power1[right_length] + right1) % MOD1
        result2 = (hash2[i] * power2[right_length] + right2) % MOD2
        hashes.add((result1, result2))

    print(len(hashes))
