MOD = 10007

comb = [[0] * 53 for _ in range(53)]

for i in range(53):
    comb[i][0] = 1

for i in range(1, 53):
    for j in range(1, 53):
        comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD

N = int(input())
ans = 0
for i in range(1, 14):
    if N - 4 * i >= 0:
        if i % 2 == 1:
            ans = (ans + comb[52 - 4 * i][N - 4 * i] * comb[13][i]) % MOD
        else:
            ans = (ans - (comb[52 - 4 * i][N - 4 * i] * comb[13][i]) % MOD + MOD) % MOD

print(ans)