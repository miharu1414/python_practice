import re

S = input()
T = 'algomethod'
reg = r'^a.*d'
result = re.sub(reg,T,S)
print(result)
