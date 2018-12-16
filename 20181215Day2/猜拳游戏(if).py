# 从控制台输⼊要出的拳 —— ⽯头（1）／剪⼑（2）／布（3）
#
# 电脑 随机 出拳 —— 先假定电脑只会出⽯头，完成整体代码功能
#
# ⽐较胜负
import random

Human = int(input("请出拳, ⽯头（1）／剪⼑（2）／布（3）"))

AI = random.randint(1, 1)

print(AI)

if (Human == 1 and AI == 2) or (Human == 2 and AI == 3) or (Human == 3 and AI == 1):
    print("Human WIN!")
elif Human == AI:
    print("No Winner!")
else:
    print("AI win!")