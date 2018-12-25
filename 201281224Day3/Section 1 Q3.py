# 3. 老师分配办公室的应用练习
#    - 输入办公室个数
#    - 输入老师的个数
#    - 然后将了老师分配到办公室，保证每个办公室至少一个
import random

office_set = []
teacher_set = []
control_flag = []
mapping_set = []
result_set = []

office_quantity = int(input('Please input a quantity of office'))
teacher_quantity = int(input('Please input a quantity of teacher'))

if teacher_quantity < office_quantity:
    quit()

for office in range(0, office_quantity):
    office_set.append('office-{number}'.format(number=office))

for teacher in range(0, teacher_quantity):
    teacher_set.append('teacher-{number}'.format(number=teacher))

control_flag = [0 for x in range(office_quantity)]

while 0 in control_flag:
    control_flag = [0 for x in range(office_quantity)]
    mapping_set = []

    for j in range(0, teacher_quantity):
        mapping_index = random.randint(0, (office_quantity - 1))
        control_flag[mapping_index] = 1
        mapping_set.append(mapping_index)

for office in office_set:
    result_set.append({office: []})

for k in range(0, len(mapping_set)):
    result_set[mapping_set[k]][office_set[mapping_set[k]]].append(teacher_set[k])

print(mapping_set)
print(result_set)