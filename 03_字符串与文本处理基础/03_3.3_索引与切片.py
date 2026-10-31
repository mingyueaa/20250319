# -*- coding: utf-8 -*-
"""
===============================================================================
 第 3 章  字符串与文本处理基础  ·  3.3 索引与切片
===============================================================================
 运行方式：python 03_3.3_索引与切片.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("3.3 索引与切片")
print("=" * 70)

text = "Python"
#         012345
#        -6-5-4-3-2-1   （负索引从 -1 开始）

print("text       =", text)
print("text[0]    =", text[0])       # P   第一个字符
print("text[-1]   =", text[-1])      # n   最后一个字符
print("text[2]    =", text[2])       # t
# C++: text[0] / text.back() / text[text.size()-1]；C++ 的负索引是未定义行为（越界）

print("\n切片 s[start:stop:step]：包含 start，不包含 stop（左闭右开）")
print("text[1:4]  =", text[1:4])      # yth   C++: text.substr(1, 3)
print("text[:3]   =", text[:3])       # Pyt   省略 start 表示从头
print("text[3:]   =", text[3:])       # hon   省略 stop 表示到尾
print("text[:]    =", text[:])        # Python 复制一份
print("text[::2]  =", text[::2])      # Pto   步长 2
print("text[::-1] =", text[::-1])     # nohtyP 步长 -1，反转字符串（C++ 需 std::reverse）
print("text[-3:]  =", text[-3:])      # hon   最后三个
print("text[:-3]  =", text[:-3])      # Pyt

# 切片越界不会报错（会被自动裁剪），但索引越界会报错
print("\ntext[2:100] =", repr(text[2:100]))   # 'thon'，不报错
print("text[100:]  =", repr(text[100:]))      # ''，不报错
try:
    text[100]
except IndexError as e:
    print("text[100] 抛异常:", e)
    # C++: std::string::at() 抛 std::out_of_range；operator[] 则是未定义行为

# 中文按"字符"索引（不是字节）
cn = "中文Python"
print("\ncn[0] =", cn[0], "| cn[-1] =", cn[-1], "| cn[2:5] =", cn[2:5])
print("len(cn) =", len(cn))          # 8 个字符
# C++: std::string 按字节索引，cn[0] 只会取到 UTF-8 的第一个字节（乱码风险）

# 切片赋值是不允许的（不可变）
try:
    text[0:2] = "PY"
except TypeError as e:
    print("切片赋值抛异常:", e)
