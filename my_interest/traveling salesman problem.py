graph = [[0 for _ in range (6)] for _ in range (6)]
b = [int(input()) for _ in range(15) ]
for i in range(5):
    j = i + 1
    while(j < 6):
        c = max(i - 1,0)
        graph[j][i] = graph[i][j] = b[5*i+ j -1 - i-c]
        j += 1
index = [1,2,3,4,5]
count = []
junban = [0,0,0,0,0]

import math
mintime = math.inf
import itertools
import copy
for pm in itertools.permutations(index):
    time = graph[0][index[0]]
    for q in range(1,5):
        time += graph[index[q-1]][index[q]]
    time += graph[index[4]][0]
    count.append(time)
    if mintime > time:
        mintime = copy.deepcopy(time)
        for n in range(5):
            junban[n] = copy.deepcopy(index[n])

for results in count:
    print(results)

print("最適ルートを通った場合の最短距離は {mintime}")
print("最短ルートは ")
print(1, junban[0], junban[1], junban[2], junban[3], junban[4],1)
