# 编程题：从键盘输入一个用户名和密码，判断是否正确，如果是则打印登录系统成功，否则显示用户名或密码错误

default_inf = {'username': 'aaa', 'password': '123'}
control_flag = 0

while control_flag == 0:
    input_username = input('Please input username: ')
    input_password = input('Please input password: ')
    if input_username == default_inf['username'] and input_password == default_inf['password']:
        print('login successfully')
        control_flag = 1
    else:
        print('invalid username or password, please try again.')
