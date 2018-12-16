# part3.num.3:编写代码，1-7七个数字，分别代表周一到周日，如果输入的数字是6或7，输出“周末”。

# day = int(input("请输入1-7任意数字"))
#
# if day == 6 or day == 7:
#     print("周末")
# elif day == 1:
#     print("周一")
# elif day == 2:
#     print("周二")
# elif day == 3:
#     print("周三")
# elif day == 4:
#     print("周四")
# elif day == 5:
#     print("周五")


# part3.num.3:编写代码，1-7七个数字，分别代表周一到周日，如果输入的数字是6或7，输出“周末”，否则输出“工作日”。

# day = int(input("请输入1-7任意数字"))
#
# if day == 6 or day == 7:
#     print("周末")
# else:
#     print('工作日')

# part3.num.3:编写代码，1-7七个数字，分别代表周一到周日，如果输入的数字是6或7，输出“周末”，
# 如果输入的数字是1-5，输出“工作日”，如输入其他数字，输出“错误”。

day = int(input("请输入1-7任意数字"))

if day == 6 or day == 7:
    print("周末")
elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
    print("工作日")
else:
    print("错误")