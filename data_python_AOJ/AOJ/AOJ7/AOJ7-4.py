n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
ans = [[0] * l for _ in range(n)]
for i in range(n):
    for k in range(l):
        for j in range(m):
             ans[i][k] += A[i][j] * B[j][k]

for i in range(n):
    print(' '.join(map(str, ans[i])))
