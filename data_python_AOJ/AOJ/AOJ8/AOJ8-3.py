c = []
while True:
    try:
        a = input()
        b = a.lower()
        c = list(b) + c  
    except EOFError:
        break

for i in range(97,123):
    print(f'{chr(i)} : {c.count(chr(i))}')

