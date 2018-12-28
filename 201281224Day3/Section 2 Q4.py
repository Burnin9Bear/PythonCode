# 编程：使用字典来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等），这些信息来自键盘的输入
user_info = {}

user_name = input('Please input your name: ')
user_info['user_name'] = user_name

user_age = int(input('Please input your age: '))
user_info['user_age'] = user_age

user_id = input('Please input your id: ')
user_info['user_id'] = user_id

print(user_info)

