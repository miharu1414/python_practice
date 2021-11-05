s = list(map(int,input().split()))
ans = []
for i in s:
    ans.append(chr(i+96))
print("".join(ans))


