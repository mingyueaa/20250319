# -*- coding: utf-8 -*-
"""
===============================================================================
 第 2 章  运算符与表达式  ·  2.8 身份运算符 is / is not、成员运算符 in / not in
===============================================================================
 运行方式：python 08_2.8_身份运算符_is_is_not_成员运算符_in_not_in.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("2.8 身份运算符 is / is not、成员运算符 in / not in")
print("=" * 70)

# ---- is：判断是不是同一个对象（比较 id） ----
p = [1, 2]
q = [1, 2]
print("p == q :", p == q)       # True  值相等
print("p is q :", p is q)       # False 不是同一个对象
print("p is not q :", p is not q)   # True
# C++: 没有直接对应。p == q 类似 operator==；is 类似比较两个指针地址。

# is 的正当用途：判断 None / True / False 这些单例
r = None
print("r is None :", r is None)

# ---- in：成员判断 ----
print("'ell' in 'hello' :", "ell" in "hello")       # True  子串
print("'x' not in 'hello' :", "x" not in "hello")   # True
print("3 in [1, 2, 3] :", 3 in [1, 2, 3])           # True
print("'k' in {'k': 1} :", "k" in {"k": 1})         # True  字典查的是"键"
print("2 in {1, 2, 3} :", 2 in {1, 2, 3})           # True
# C++: 字符串有 find() != npos；容器有 std::find(...) != end()；
#      关联容器有 count()/contains()（C++20）。Python 的 in 统一且更自然。
