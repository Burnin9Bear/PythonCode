# 用户名和密码格式校验程序
#
# - 要求从键盘输入用户名和密码，校验格式是否符合规则，如果不符合，打印出不符合的原因，并提示重新输入
# - 用户名长度6-20，用户名必须以字母开头
# - 密码长度至少6位，不能为纯数字，不能有空格

control_flag_u = 0
control_flag_p = 0

while control_flag_u == 0:
    input_username = input('Please input username: ')
    if input_username[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if 20 >= len(input_username) >= 6:
                control_flag_u = 1
                while control_flag_p == 0:
                    input_password = input('Please input password: ')
                    if not input_password.isdigit():
                        if len(input_password) > 6:
                            print('register successfully')
                            control_flag_p = 1
                        else:
                            print('Password must be at least 6 characters long')
                    else:
                        print('password must be include a letter character')
            else:
                print('username include a minimum of 6 characters and maximum of 20 characters ')
    else:
        print('the first character must bu a letter')