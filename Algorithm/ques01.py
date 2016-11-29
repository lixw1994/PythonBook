# encoding: utf-8

"""
@version: ??
@author: 李宪伟
@license: Apache Licence 
@contact: lixw1994@yeah.net
@site: 
@software: PyCharm
@file: ques01.py
@time: 2016/11/29 上午9:21
"""

# Q: 我们有一个包含N个元素的元组或者序列,现在想将它分解为N个单独变量

# R: 任何序列(或可迭代的对象)都可以通过一个简单的赋值操作来分解为单独的变量.
#     唯一的要求是变量的总数和结构要与序列相吻合.

def test():
    p = (4, 5)
    x, y = p
    print(x, y)

    data = ['ACME', 50, '91.9', (2012, 12, 24)]
    name, shares, price, date = data
    print(name, shares, price, date)

    # 可分解的不仅仅是元组和列表,只要对象是可迭代的(字符串,文件,迭代器,生成器),都可以分解.
    str = "hello"
    a, b, c, d, e = str
    # 如果数量不匹配会出现错误
    # a, b, c, d = str   错误
    print(a, b, c, d, e)

    # 如果对某一个分解变量不感兴趣, 可以用一个唯一的变量保存但是不适用的方法
    point = (3, 4)
    _, y = point
    print y


if __name__ == '__main__':
    test()