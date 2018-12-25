# 1. 从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母
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
for name_temp in name_set:
    print(name_temp[1])


