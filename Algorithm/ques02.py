# encoding: utf-8

'''
Title: 从任意长度的可迭代对象中分解元素
Ques:  需要从某个可迭代对象中分解出N个元素,但是这个可迭代对象的长度可能超过N,
        可能会导致分解值过多(too many values to unpack)的异常
Answ:  利用Python的 * 表达式(只能用于python 3.x)
'''

def test():
    record = ('david', 'lixw@@', '6332333', '1326443')
    name, email, *phone1 = record
    print(phone1)

    # 忽略不感兴趣的项目
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name, year)


if __name__ == '__main__':
    test()