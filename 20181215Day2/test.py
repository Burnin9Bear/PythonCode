import random


while True:  # 死循环完美写法

    # 玩家出的拳
    player = int(input("石头（1）／剪刀（2）／布（3）："))
    # 电脑出的拳
    computer = random.randint(1, 3)

    # 判断玩家胜利的条件
    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):

        print("玩家胜利")
        break
    elif player == computer:

        print("平局")

    else:
        print("电脑胜利")
