# 黑马程序员全套Python教程_Python基础入门视频教程，零基础小白自学Python入门教程
# https://www.bilibili.com/video/BV1o4411M71o?p=1&vd_source=8fd2de1d80aed33dc7cfc2afe1e694a0

# P09 09-新建书写运行文件
print('Hello World!')  # '与''相同

# P14 14-注释
# 单行注释

'''
多行注释1
多行注释2
'''

"""
多行注释3
多行注释4
"""

# P20 20-认识数据类型
# int-数值整型 float-数值浮点型 布尔型（True False） str-字符串 list-列表 tuple-元组 set-集合 dict-字典（键值对）
num1 = 1
num2 = 1.1
print(type(num1))
print(type(num2))
a = 'Hello World'
print(type(a))
b = True
print(type(b))
c = [10, 20, 30]
print(type(c))
d = (10, 20, 30)
print(type(d))
e = {10, 20, 30}
print(type(e))
f = {'name': 'Tom', 'age': 18}
print(type(f))

# P22 01-输出_认识格式化符号
# %s-字符串 %d-有符号的十进制整数 %f-浮点数 %c-字符 %u-无符号的十进制整数 %o-八进制整数
# %x-十六进制整数（小写ox） %X-十六进制整数（大写写OX） %e-科学计数法（小写‘e’） %E-科学计数法（大写‘E’） %g-%f和%e的简写 %G-%f和%E的简写

# P24 03-输出_格式化符号高级使用方法
# %06d-输出的整数显示位数，不足以0补全，超出当前位数则原样输出 %.2f-小数点后显示的小数位数
age = 18
name = 'Tom'
weight = 75.5
stu_id = 121101221885
print('我的名字是%s，明年%d岁了，体重%.1f公斤，学号是%015d。' % (name, age + 1, weight, stu_id))
print('我的名字是%s，明年%s岁了，体重%s公斤，学号是%015s。' % (name, age + 1, weight, stu_id))
print(f'我的名字是{name}，明年{age + 1}岁了，体重{weight}公斤，学号是{stu_id:015}。')

# P27 06-输出_转义字符
# \n-换行 \t-制表符（一个tab为四个空格距离）
print('Hello\nWorld')
print('Hello World')
print('\tHello World')

# P28 07-输出_print的结束符
print(end='\n')
print('Hello', end='\n')
print('world', end='...')
print('Hello', end='\t')
print('world')
