import sys
s = []
while True:
    l = input()
    if l == '0':
        break
    s.append(l)

for i in s:
    keta = list(map(int, i))
    print(sum(keta))
