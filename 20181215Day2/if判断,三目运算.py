# if 判断分数

score = input("请输入分数")

score = int(score)

if score >= 140:
    print("超越了99%的学生")
elif score >= 120:
    print("超越了80%的学生")
elif score >= 90:
    print("超越了30%的学生")
else:
    print("请努力学习")

# 三目运算法:

Alex = int(input("请输入Alex杀敌数"))

Charlie = int(input("请输入Charlie杀敌数"))

King = "Alex是全场最佳" if Alex > Charlie else "Charlie是全场最佳"

print(King)