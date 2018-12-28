# 完成字符串的逆序以及统计
#
# - 设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
# - 打印出字符串长度
# - 使用切片逆序打印出字符串

control_flag = 0

while control_flag == 0:
    input_str = input('please input a string: ')
    if len(input_str) > 31:
        print(' string must be at most 31 characters long, please try again')
    else:
        str_length = len(input_str)
        reverse_str = input_str[::-1]
        print('the length of string is %d' %str_length)
        print('the reverse of string is %s'%reverse_str)
        control_flag = 1


