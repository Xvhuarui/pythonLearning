# 黑马程序员全套Python教程_Python基础入门视频教程，零基础小白自学Python入门教程
# https://www.bilibili.com/video/BV1o4411M71o?p=1&vd_source=8fd2de1d80aed33dc7cfc2afe1e694a0

# P84 19-for循环语法和体验
s1 = '''I\'T
heima'''
for i in s1:
    print(i, end=' ')

# P100 07-体验切片
s2 = 'HelloWorld'
print(s1)
print()
print(s2[0])
print()
print(s2[-4:-8:-1])  # 选取方向不要与步长方向冲突

# P102 09-字符串常用操作的方法之查找
# .find(子串, 开始位置下标,结束位置下标)-找不到返回-1 .index()-找不到会报错 .count()-个数
# P103 10-~修改
# .replace(旧子串, 新子串, 替换次数)-字符串是不可变数据类型（修改不了） .split(分割字符, num)-返回列表数据 .join()-合并列表里字符串数据
# P104 11-~大小写转换
# .capitalize()-字符串首字母大写 .title()-每个单词首字母大写 .upper()-小写转大写 .lower()-大写转小写
# P105 12-~删除空白字符
# .lstrip()-删除字符串左侧空白字符 .rstrip()-删除字符串右侧空白字符 .strip()-删除字符串两侧空白字符
# P106 13-~字符串对齐
# .ljust(长度, 填充字符)-左对齐 .rjust()-右对齐 .center()-中间对齐
# P107 14-~判断开头或结尾
# .startswith(子串, 开始位置下标, 结束位置下标)-返回布尔型数据 .endswith()
# P108 15-~判断
# .isalpha()-是否都是字母 .isdigit()-是否都是数字 .isalnum()-是否都是数字、字母或组合 .isspace()-是否都是空白
