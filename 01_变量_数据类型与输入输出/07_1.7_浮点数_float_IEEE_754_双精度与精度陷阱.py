# -*- coding: utf-8 -*-
"""
===============================================================================
 第 1 章  变量、数据类型与输入输出  ·  1.7 浮点数 float：IEEE 754 双精度与精度陷阱
===============================================================================
 运行方式：python 07_1.7_浮点数_float_IEEE_754_双精度与精度陷阱.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("1.7 浮点数 float：IEEE 754 双精度与精度陷阱")
print("=" * 70)

pi = 3.14159
sci = 1.5e3              # 科学计数法：1500.0
tiny = 1e-3              # 0.001
print("pi =", pi, "| sci =", sci, "| tiny =", tiny)
# C++: double 与 Python float 都是 IEEE 754 double（64 位），精度一致

# 经典精度问题：0.1 + 0.2 并不严格等于 0.3
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3 ?", 0.1 + 0.2 == 0.3)   # False！
# C++: 同样的问题，double a = 0.1 + 0.2; a == 0.3 也是 false

# 正确做法 1：用 math.isclose 做"近似相等"比较
import math
print("math.isclose(0.1 + 0.2, 0.3) =", math.isclose(0.1 + 0.2, 0.3))

# 正确做法 2：涉及金额等精确十进制场景，用 decimal.Decimal
from decimal import Decimal
print("Decimal('0.1') + Decimal('0.2') =", Decimal("0.1") + Decimal("0.2"))
# C++: 没有内置十进制类型，通常自己封装或用第三方库

# 特殊值
print("float('inf')  =", float("inf"))      # 无穷大   C++: std::numeric_limits<double>::infinity()
print("float('-inf') =", float("-inf"))
print("float('nan')  =", float("nan"))      # 非数     C++: std::numeric_limits<double>::quiet_NaN()
print("math.isnan(float('nan')) =", math.isnan(float("nan")))

# 取整相关：int() 向零截断；round() 是"四舍六入五成双"（银行家舍入）
print("int(3.9) =", int(3.9), "| int(-3.9) =", int(-3.9))
print("round(2.5) =", round(2.5), "| round(3.5) =", round(3.5))   # 2 和 4
# C++: static_cast<int>(3.9) 也是向零截断；std::round(2.5) 则是 3（远离零），行为不同！
