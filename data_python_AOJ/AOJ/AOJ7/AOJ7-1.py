def grade(m, r, f):
    if m == -1 or r == -1:
        return 'F'
    elif m + r >= 80:
        return 'A'
    elif m + r >= 65:
        return 'B'
    elif m + r >= 50:
        return 'C'
    elif m + r >= 30:
        if f >= 50:
            return 'C'
        else:
            return 'D'
    else:
        return 'F'



while True:
    m, r, f = map(int, input().split())
    if m == -1 and r == -1 and f == -1:
        break
    print(grade(m, r, f))