# 黑马程序员全套Python教程_Python基础入门视频教程，零基础小白自学Python入门教程
# https://www.bilibili.com/video/BV1o4411M71o?p=1&vd_source=8fd2de1d80aed33dc7cfc2afe1e694a0

# P169 02-函数的使用步骤
# 定义：def 函数名(参数) 调用：函数名(参数)
def info_print():
    print('hello world')


info_print()


# P172 05-函数的参数的作用
# 定义函数中a和b为形参，调用函数的10和20为实参
def add_num2(a, b):
    result = a + b
    print(result)


add_num2(10, 20)


# P173 06-体验函数返回值
# 返回值用于赋值，return即退出当前函数
def buy():
    return '烟'


goods = buy()
print(goods)
