# -*- coding: UTF-8 -*-
# 使用while循环计算1~100的累积和（包含1和100）。

summary = 0
i = 1
while i <= 100:
    summary += i
    i += 1
print(summary)

# 计算1~100之间偶数的累积和（包含1和100）

summary = 0
i = 0
while i <= 100:
    summary += i
    i += 2
print(summary)

# 使用while循环计算5!（5的阶乘）。

summary = 1
i = 5
while i > 0:
    summary *= i
    i -= 1
print(summary)

# 从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!(3!的意思就是3的阶乘)的结果，并输出

summary = 1
ic = int(input('please input a number: '))
i = ic
while i > 0:
    summary *= i
    i -= 1
print("%2d! = %2d " % (i, summary))

# 使用while循环输出如下图形：
# *
# * *
# * * *
# * * * *
# * * * * *

tiers = 5
tier_c = 0
while tier_c < tiers:
    stars = tier_c + 1
    spaces = tier_c
    raw_c = 0
    while raw_c < stars + spaces:
        if raw_c % 2 == 0:
            print('*', end='')
        elif raw_c % 2 != 0:
            print(' ', end='')
        raw_c += 1
    print('')
    tier_c += 1

# 使用while循环输出如下图形：
# * * * * *
# * * * *
# * * *
# * *
# *

tiers = 5
tier_c = 0
while tier_c < tiers:
    stars = tiers - tier_c
    spaces = tiers - tier_c - 1
    raw_c = 0
    while raw_c < stars + spaces:
        if raw_c % 2 == 0:
            print('*', end='')
        elif raw_c % 2 != 0:
            print(' ', end='')
        raw_c += 1
    print('')
    tier_c += 1

# 使用循环嵌套打印九九乘法表。

tiers = 9
rows = 0
while rows < 9:
    column = 0
    while column < rows + 1:
        print(" |%2d x %2d = %2d" % ((column + 1), (rows + 1), ((rows + 1) * (column + 1))), end='')
        column += 1
    print('')
    rows += 1

# 设计“过7游戏”的程序, 打印出1-100之间除了含7和7的倍数之外的所有数字。

number = 100
i = 0
while i < 100:
    i += 1
    if i % 7 == 0:
        print('')
        continue
    print("%d " % i, end='')

# 使用while，完成以下图形的输出

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

tier_temp = int(input('please input tier: '))
tier = tier_temp + 1
middle = 0
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
        else:
            print('*', end='')
        k += 1
    print('')
    i += 1