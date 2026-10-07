import sys

data = sys.stdin.buffer.read().split()
n = int(data[0])
m = int(data[1])
words = data[2:2 + n]
queries = data[2 + n:]
MOD1 = 10 ** 9 + 7
MOD2 = 10 ** 9 + 9
BASE = 31
max_length = max(map(len, data[2:]), default=0)
power1 = [1] * (max_length + 1)
power2 = [1] * (max_length + 1)

for i in range(max_length):
    power1[i + 1] = power1[i] * BASE % MOD1
    power2[i + 1] = power2[i] * BASE % MOD2


def get_hash(s):
    hash1 = 0
    hash2 = 0
    for ch in s:
        value = ch - 96
        hash1 = (hash1 * BASE + value) % MOD1
        hash2 = (hash2 * BASE + value) % MOD2
    return hash1, hash2


dictionary = set()

for word in words:
    hash1, hash2 = get_hash(word)
    dictionary.add((len(word), hash1, hash2))

answers = []

for query in queries:
    length = len(query)
    hash1, hash2 = get_hash(query)
    found = False

    for i in range(length):
        old_value = query[i] - 96
        degree = length - i - 1

        for new_value in range(1, 4):
            if new_value == old_value:
                continue
            new_hash1 = (hash1 + (new_value - old_value) * power1[degree]) % MOD1
            new_hash2 = (hash2 + (new_value - old_value) * power2[degree]) % MOD2

            if (length, new_hash1, new_hash2) in dictionary:
                found = True
                break

        if found:
            break

    answers.append("YES" if found else "NO")

sys.stdout.write("\n".join(answers))
