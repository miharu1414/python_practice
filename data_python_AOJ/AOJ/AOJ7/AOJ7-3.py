r, c = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r)]

R = []
C = [0] * (c + 1)
for i in range(r):
    sumc = 0
    for j in range(c):
        sumc += A[i][j]
        C[j] += A[i][j]
    R.append(sumc)
    C[c] += sumc

for i in range(r):
    print(' '.join(map(str, A[i])), R[i])
print(' '.join(map(str, C)))