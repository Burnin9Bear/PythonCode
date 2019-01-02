# 设计一个程序，实现str.split()方法的替换：
#
# - 首先输入一个任意长度的字符串
# - 其次输入一个字符，用以分割该字符串，并且分割后的字符串保存到一个列表中
# - 不允许使用str.split()方法
# - 最后打印出该字符串被分割成多少部分、以及这个列表
# - 去掉分割出来的空字符串
# - 如"1234r5678r90r"用r分割，则为["1234","5678","90"]

result = []
str1 = input('Please input a string')
str2 = input('please input a string to split the first string')

# repeat = str1.count(str2)
#
# if repeat > 0:
#     last_index = 0
#     for i in range(0, repeat ):
#         current_index = str1.find(str2, last_index)
#         print(last_index)
#         print(current_index)
#         if last_index != current_index:
#             result.append(str1[last_index: current_index])
#         last_index = current_index + 1
# else:
#     result.append(str1)
#
# print(result)


temp_str = ''
for i in str1:
    if i == str2:
        if temp_str:
            result.append(temp_str)
            temp_str = ''
        continue
    temp_str += i
if temp_str:
    result.append(temp_str)

print(str1.split(str2))
print(result)