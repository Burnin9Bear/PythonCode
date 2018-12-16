num1 = int(input("请输入第一个数字"))
num2 = int(input("请输入第二个数字"))
num3 = int(input("请输入第三个数字"))

sum = num1 + num2 +num3

if sum >100000:
    print("您输入的三个数的和忒大了")

elif sum >10000:
    print("您输入的三个数的和挺大")

elif sum >1000:
    print("您输入的三个数的和有点大")

elif sum >100:
    print("您输入的三个数的和不算大")

elif sum <=100:
    print("您输入的三个数的和忒小了")