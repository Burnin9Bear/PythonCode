# name = "小明"
# print("我的名字是%s" % name)

# student_no = "00001"
# print("我的学号是%06d" % student_no)
# print("我的学号是 %06d" % student_no)

# price = float(input("请输入苹果的价格"))
# weight = float(input("请输入苹果的重量"))
# pay = (price * weight)
# print("苹果总共是:%.2f元" % pay)

# c = input(5666)
# print("c = %s" % c)
#
# age = int(input("请输入年龄"))
# if age >= 18 and age < 100:
#     print("已成年")
# elif age <18 and age > 0:
#     print("未成年")
# else: print("请输入正确的年龄")

# coding=utf-8
# 定义字符串变量temp1
temp1 = "hello python"
# 接收用户的输入
temp2 = input("请输入：")
# 定义数字变量temp3
temp3 = 333
# 定义字符串变量temp4
temp4 = 333
# 求和
temp5 = temp3 + temp4

if temp5 == 666:
    print("%s + %s = %s, 挺溜啊"%(temp3,temp4,temp5))
if temp5 != 666:
    print("一点儿也bu溜")
print("您刚刚输入的是:%s"%temp2)