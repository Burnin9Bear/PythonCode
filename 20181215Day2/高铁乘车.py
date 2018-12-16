Ticket = False

knifeLenth = 88

if Ticket:
    print("请进行安检")
    if knifeLenth > 9:
        print("请换一把刀")
    else:
        print("可以进行乘车")
else:
    print("请购票")