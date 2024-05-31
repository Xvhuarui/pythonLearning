# 黑马程序员全套Python教程_Python基础入门视频教程，零基础小白自学Python入门教程
# https://www.bilibili.com/video/BV1o4411M71o?p=1&vd_source=8fd2de1d80aed33dc7cfc2afe1e694a0

# P60 15-猜拳游戏步骤分析
import random

player = input('请做出选择：')
print(f'你的选择是：{player}')
comp = ['石头', '剪刀', '布']
C = random.choice(comp)  # random.randint(开始, 结束)
print(f'电脑的选择是：{C}')
if player == '布':
    if C == '石头':
        print('Player win!')
    elif C == '剪刀':
        print('Player lose!')
    else:
        print('Continue!')
elif player == '剪刀':
    if C == '石头':
        print('Player lose!')
    elif C == '剪刀':
        print('Continue!')
    else:
        print('Player win!')
else:
    if C == '石头':
        print('Continue!')
    elif C == '剪刀':
        print('Player win!')
    else:
        print('Player lose!')
print('游戏结束！')

# P64 19-三目运算符
# 条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
a = 1
b = 2
c = a - b if a > b else b - a
print(c)
