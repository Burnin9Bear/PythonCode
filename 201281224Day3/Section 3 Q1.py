# 有10个球分别3红、3蓝、4白，现需要将这10个球放入这3个盒子，要求每个盒子至少有一个白球，请用程序实现

import random
box_set = []
red_ball_set = []
blue_ball_set = []
white_ball_set = []
result_set = {}

for i in range(0, 3):
    box_set.append('box-{id}'.format(id=i))
    red_ball_set.append('red-{id}'.format(id=i))
    blue_ball_set.append('blue-{id}'.format(id=i))

for i in range(0, 4):
    white_ball_set.append('white-{id}'.format(id=i))

for box in box_set:
    white_pop_index = random.randint(0, len(white_ball_set) - 1)
    result_set[box] = [white_ball_set.pop(white_pop_index)]

mixture_set = red_ball_set + blue_ball_set + white_ball_set

del red_ball_set
del white_ball_set
del blue_ball_set

for i in range(0, len(mixture_set)):
    box_index = random.randint(0, len(box_set) - 1)
    result_set['box-{id}'.format(id=box_index)].append(mixture_set.pop(0))

print(result_set)