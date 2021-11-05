h, w = map(int, input().split())
dp = [list(map(int,input().split())) for l in range(h)]
ans = [[0 for _ in range(w)] for _ in range(h)]
row = []
col = []
for i in range(h):
    row.append(0)
    for j in range(w):
        row[i]+= dp[i][j]
for i in range(w):
    col.append(0)
    for j in range(h):
        col[i]+= dp[j][i]

for i in range(h):
    for j in range(w):
        ans[i][j] = col[j]+row[i]-dp[i][j]


for i in range(h):
    ans[i] = [str(j) for j  in ans[i]]
    print(" ".join(ans[i]))

