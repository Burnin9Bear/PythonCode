# 从键盘获取5个学生的名字，然后随机抽出一名学生去打扫卫生
import random
name_set = []
name1 = input("input the first student's name")
name_set.append(name1)
name2 = input("input the second student's name")
name_set.append(name2)
name3 = input("input the third student's name")
name_set.append(name3)
name4 = input("input the forth student's name")
name_set.append(name4)
name5 = input("input the fifth student's name")
name_set.append(name5)
print('%s is going to do some cleaning' % name_set[random.randint(0, len(name_set))])
