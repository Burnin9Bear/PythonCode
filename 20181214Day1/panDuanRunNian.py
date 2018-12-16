Year = int(input("请输入年份"))
if Year % 4 == 0  and Year % 100 == 1:
    print("%d年是闰年"%Year)
elif Year % 400 == 0:
     print("%d年是闰年"%Year)
else:
    print("%d年不是闰年"%Year)