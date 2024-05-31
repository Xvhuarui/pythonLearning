# 黑马程序员全套Python教程_Python基础入门视频教程，零基础小白自学Python入门教程
# https://www.bilibili.com/video/BV1o4411M71o?p=1&vd_source=8fd2de1d80aed33dc7cfc2afe1e694a0

# P113 04-判断是否存在
# print('' in 列表) not in-返回布尔型
name_list = ['Tom', 'Bobby', 'Lily', 'Rose']
name = input('请输入注册姓名：')
if name not in name_list:
    print('注册成功！')
    name_list.append(name)
    print(name_list)
else:
    while name in name_list:
        print('名字已存在，请重新注册')
        name = input('请输入注册姓名：')
        if name not in name_list:
            print('注册成功！')
            name_list.append(name)
            print(name_list)
            break

# P115-117 06.07.08-列表增加数据之append.extend.insert
# .append(数据)-列表结尾追加数据，不改变数据类型 .extend（）-序列会被拆开 .insert(位置下标, 数据)
# P118 09-列表删除数据
# .del 目标-全部删除 .pop(下标)-删除指定下标数据（默认为最后一个）并返回该数据 .remove(数据)-删除指定数据 .clear()-清空列表
# P119 10-列表修改数据
# .reverse()-逆置 .sort(key = None, reverse = False)-key与字典有关，True降序，False升序默认
# P120 11-列表复制数据
# .copy()
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1
for i in name_list:
    print(i)
