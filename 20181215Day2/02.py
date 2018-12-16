weight = float(input("请输入苹果重量"))
price = float(input("请输入苹果价格"))
money = weight * price
print("您购买了%.2f斤苹果，苹果一斤%.2f元，总共是%.2f元" % (weight , price , money))