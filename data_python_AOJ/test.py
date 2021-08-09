xy = [list(map(int, input().split())) for _ in range(5)]
x, y = [list(i) for i in zip(*xy)]
print(x)