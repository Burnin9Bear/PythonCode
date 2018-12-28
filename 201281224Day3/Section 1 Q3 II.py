# 3. 老师分配办公室的应用练习
#    - 输入办公室个数
#    - 输入老师的个数
#    - 然后将了老师分配到办公室，保证每个办公室至少一个

import random
control_flag = 0
office_quantity, teacher_quantity = 0, 0
office_set = []
teacher_set = []
result_set = []

while control_flag == 0:
    office_quantity = int(input('Please input a quantity of office'))
    teacher_quantity = int(input('Please input a quantity of teacher'))
    if teacher_quantity >= office_quantity:
        control_flag = 1
    else:
        print("The quantity of teacher must be larger than office's!!")

for office in range(0, office_quantity):
    office_set.append('office-{number}'.format(number=office))

for teacher in range(0, teacher_quantity):
    teacher_set.append('teacher-{number}'.format(number=teacher))

for office in office_set:
    pop_teacher_index = random.randint(0, len(teacher_set) - 1)
    pop_teacher = teacher_set.pop(pop_teacher_index)
    result_set.append({office: [pop_teacher]})


while len(teacher_set) > 0:
    office_index = random.randint(0, office_quantity - 1)
    result_set[office_index]['office-{number}'.format(number=office_index)].append(teacher_set.pop())

print(result_set)