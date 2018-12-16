# coding = utf-8
tier_temp = int(input('please input tier: '))
tier = tier_temp + 1
if tier % 2 == 0:
    middle = tier / 2
else:
    print("tier must be an odd")
    exit(100)
i = 0
while i <= tier:
    if i < middle:
        star = 2 * i - 1
    else:
        star = 2 * (tier - i) - 1
    j, k = 0, 0
    while k < star:
        if i < middle:
            space = middle - i
        else:
            space = i - middle
        while j < space:
            print(' ', end='')
            j += 1
        if k == star - 1:
            print('*')
        else:
            print('*', end='')
        k += 1
    i += 1
