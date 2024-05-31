# 黑马程序员全套Python教程_Python基础入门视频教程，零基础小白自学Python入门教程
# https://www.bilibili.com/video/BV1o4411M71o?p=1&vd_source=8fd2de1d80aed33dc7cfc2afe1e694a0

# P83 18-while循环嵌套应用之九九乘法表
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i}*{j}=', end='')
        print(i * j, end='\t')
        if i == j:
            print()
            break
        i += 1
    j += 1
