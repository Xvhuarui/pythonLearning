# 黑马程序员全套Python教程_Python基础入门视频教程，零基础小白自学Python入门教程
# https://www.bilibili.com/video/BV1o4411M71o?p=1&vd_source=8fd2de1d80aed33dc7cfc2afe1e694a0

# P46 01-if的作用于语法
ID = input('请输入身份证：')
Y = int(ID[6:10])
print(Y)
if Y > 2024 or len(str(ID)) != 18:
    print('输入错误！请重新输入。')
else:  # 可直接elif-else if
    if 2024 - Y < 18:
        print('禁止进入！')
    else:
        print('祝您上网愉快！')
print('系统关闭。')
