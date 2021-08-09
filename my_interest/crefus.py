adv1 = [0, 0, 0, 0, 0, 0]
cnt = 0
while True:
    a = input()
    if (a == 'end'):
        break
    cnt += 1
    if (a == '1'):
        adv1[0] += 1
    elif (a == '2'):
        adv1[1] += 1
    elif (a == '3'):
        adv1[2] += 14
    elif (a == '4'):
        adv1[3] += 1
    elif (a == '5'):
        adv1[4] += 1
    elif (a == '6'):
        adv1[5] += 1

print(adv1)
print(f'チラシ:{adv1[0]} 新聞:{adv1[1]} DM:{adv1[2]}')
print(f'HP:{adv1[3]} 教室前掲示板:{adv1[4]} 知人紹介:{adv1[5]} 合計回答数:{cnt}')
