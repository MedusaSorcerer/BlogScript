#!/usr/bin/python3
# _*_ Coding: UTF-8 _*_
"""
    Date: 2021/12/26
"""
import datetime as datetime

# 直接输出变量名，让你的代码更加简单，语法是基于 Python3.10
string = 'Hello Medusa'
print(f'{string = }')

# 直接对结果进行计算改变输出，语法是基于 Python3.10
number = 1024
print(f'{number % 1 =}')

# 直接对事件对象进行格式化输出，语法是基于 Python3.10
datetime = datetime.datetime.now()
print(f'{datetime:%Y-%m-%d %H:%M:%S}')

# 进制转换输出，语法是基于 Python3.10
number_10 = 1024
print(f'{number_10:b}')  # 2进制
print(f'{number_10:o}')  # 8进制
print(f'{number_10:x}')  # 16进制小写
print(f'{number_10:X}')  # 16进制大写
print(f'{number_10:c}')  # ASCII编码

# 格式化浮点数，语法是基于 Python3.10
number_float = 1024.123
print(f'{number_float = :.2f}')  # 保留小数点两位小数
number_float_format = '.3f'
print(f'{number_float:{number_float_format}}')  # 参数嵌套，保留小数点三位小数

# 字符串对其，语法是基于 Python3.10
text = 'Medusa'
print(f'{text:>10}')  # 右对齐
print(f'{text:<10}')  # 左对齐
print(f'{text:^10}')  # 居中对齐
print(f'{text:*^10}')  # 居中对齐，用*补齐空白
n = 10
print(f'{text:~^{n}}')  # 参数嵌套，居中对齐，用~补齐空白

# !s 和 !r，语法是基于 Python3.10
text = 'Medusa'
print(f'{text!s}')  # str(text)
print(f'{text!r}')  # repr(text)

# 自定义格式，语法是基于 Python3.10


class MedusaFormatString:
    def __format__(self, format_spec):
        return format_spec


print(f'{MedusaFormatString():&1&2}')
