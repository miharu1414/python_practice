import itertools
ans = []
while True:
    n, x = map(int, input().split())
    cnt = 0
    if n == 0 and x == 0:
        break
    sample = []
    for j in range(n):
        sample.append(j + 1)
    for i in itertools.combinations(sample, 3):
        a, b, c = i
        if a + b + c == x:
            cnt += 1
    ans.append(cnt)
for i in ans:
    print(i)
