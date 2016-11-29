# encoding: utf-8

"""
Title: 保存最后N个元素
Q:  我们希望在迭代或者是其他形式的处理中对最后几项记录做一个有限的历史记录统计
A:  collections.deque的完美应用场景
"""

# 下面的程序做简单的文本匹配操作,发现有匹配项时输出当前的匹配行以及最后检查的N行文本

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    pass