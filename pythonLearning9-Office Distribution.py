# 黑马程序员全套Python教程_Python基础入门视频教程，零基础小白自学Python入门教程
# https://www.bilibili.com/video/BV1o4411M71o?p=1&vd_source=8fd2de1d80aed33dc7cfc2afe1e694a0

# P124 15-随机分配办公室的步骤分析
import random
Teachers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
Office = [[], [], []]
for name in Teachers:
    num = random.randint(0, 2)
    Office[num].append(name)
i = 1
for Off in Office:
    print(f'办公室{i}人数为{len(Off)}，分别为：')
    for na in Off:
        print(na)
    i += 1
