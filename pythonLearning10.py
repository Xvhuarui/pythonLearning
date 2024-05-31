# 黑马程序员全套Python教程_Python基础入门视频教程，零基础小白自学Python入门教程
# https://www.bilibili.com/video/BV1o4411M71o?p=1&vd_source=8fd2de1d80aed33dc7cfc2afe1e694a0

# 字典是键值对{}

# P138 06-字典常用操作之查找
# .get(key, 默认值)-若当前查找的key不存在则返回第二个参数（默认值），如果省略第二个参数，则返回None
# .keys() .values() .items()-返回里面的数据是元组，元组数据可以拆包返回多个数据

# P143 12-创建集合
# set()-创建空集合 {}-创建空字典 集合重点在于去重复 集合是无序的

# P144 13-集合常见操作之增加数据
# .add()-增加单个数据 .update()-增加序列
# P115 14-集合常见操作之删除数据
# .remove()-删除指定数据，数据不存在报错 .discard()-删除指定数据，数据不存在不报错 .pop()-随机删除

# P148-150 01.02.03-公共操作之运算符
#     +        合并         字符串、列表、元组
#     *        复制         字符串、列表、元组
#     in    元素是否存在   字符串、列表、元组、字典
#   not in 元素是否不存在  字符串、列表、元组、字典
# P151-155 04.05.06.07.08-公共方法
# len() del或del() max() min() range(start, end, step)-返回range类型，配合for循环输出数据
# enumerate(可遍历对象, start = 0)-函数用于将一个可遍历的数据对象组合为一个索引序列
print(type(range(1, 10, 1)))
list1 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list1):
    print(i)
for index, char in enumerate(list1,start=1):
    print(f'下标为{index}，对应字符为{char}')

# P156 09-容器类型转换
# tuple()-转换为元组 list()-转换为列表 set()-转换为集合
