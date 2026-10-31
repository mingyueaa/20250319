# -*- coding: utf-8 -*-
"""
===============================================================================
 第 2 章  运算符与表达式  ·  2.3 比较运算符（含链式比较）
===============================================================================
 运行方式：python 03_2.3_比较运算符_含链式比较.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("2.3 比较运算符（含链式比较）")
print("=" * 70)

x, y = 3, 5
print("x <  y  :", x < y)
print("x >= y  :", x >= y)
print("x == y  :", x == y)      # 比较"值"
print("x != y  :", x != y)

# 字符串比较：按 Unicode 码点逐字符比较（字典序）
print("'apple' < 'banana' :", "apple" < "banana")     # True
print("'Z' < 'a' :", "Z" < "a")                       # True（'Z'=90, 'a'=97）
# C++: std::string 的 operator< 也是字典序，结果一致

# ---- 链式比较：数学写法直接可用 ----
age = 25
print("18 <= age < 60 :", 18 <= age < 60)     # True
# 等价于 (18 <= age) and (age < 60)，但 age 只求值一次
# C++: 18 <= age < 60 会被解析成 (18 <= age) < 60，即 true < 60，语义完全错误！

# ---- 比较浮点数：不要用 == ----
import math
print("0.1 + 0.2 == 0.3 :", 0.1 + 0.2 == 0.3)                 # False
print("math.isclose(...) :", math.isclose(0.1 + 0.2, 0.3))    # True

# ---- 特殊值比较 ----
nan = float("nan")
print("nan == nan :", nan == nan)        # False！NaN 不等于自身
print("nan != nan :", nan != nan)        # True
print("math.isnan(nan) :", math.isnan(nan))
# C++: 同样如此（IEEE 754 规定）

# 判断 None 用 is，不要用 ==
value = None
print("value is None :", value is None)
