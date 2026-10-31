# -*- coding: utf-8 -*-
"""
===============================================================================
 第 2 章  运算符与表达式  ·  2.13 综合实例
===============================================================================
 运行方式：python 13_2.13_综合实例.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

import math

print("=" * 70)
print("2.13 综合实例")
print("=" * 70)

# ---- 实例 1：秒数转 时:分:秒（// 和 % 的经典用法）----
total_seconds = 3725
hours = total_seconds // 3600
minutes = total_seconds % 3600 // 60
seconds = total_seconds % 60
print(f"{total_seconds} 秒 = {hours:02d}:{minutes:02d}:{seconds:02d}")
# C++: int h = t / 3600; int m = t % 3600 / 60; int s = t % 60;

# ---- 实例 2：判断闰年（逻辑运算符 + 取余）----
def is_leap(year):
    """闰年：能被 4 整除且不能被 100 整除，或者能被 400 整除。"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    # C++: return (y % 4 == 0 && y % 100 != 0) || (y % 400 == 0);

for y in (1900, 2000, 2024, 2025):
    print(f"{y} 是闰年? {is_leap(y)}")

# ---- 实例 3：温度转换（复合赋值 + 格式化）----
celsius = 36.6
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
# C++: double f = c * 9.0 / 5.0 + 32.0;

# ---- 实例 4：不用临时变量交换 + 位运算判断奇偶 ----
a1, b1 = 11, 22
a1 ^= b1
b1 ^= a1
a1 ^= b1
print("异或交换后:", a1, b1)          # 22 11
# C++: 完全相同的技巧（注意 a、b 不能是同一个对象）

for k in range(5):
    print(f"{k} 是{'奇' if k & 1 else '偶'}数", end="  ")
print()

# ---- 实例 5：四舍五入到指定小数位（round 的半偶舍入陷阱）----
print("\nround 陷阱：")
for val in (0.5, 1.5, 2.5, 3.5):
    print(f"round({val}) = {round(val)}", end="   ")
print("\n# 2.5 -> 2 而不是 3：round 是银行家舍入（半偶舍入）")
# C++: std::round(2.5) == 3（远离零）；std::nearbyint(2.5) == 2（受舍入模式控制）

# 需要"传统四舍五入"时的写法（对正数）：floor(x + 0.5)
print("floor(2.5 + 0.5) =", math.floor(2.5 + 0.5))
# C++: std::floor(x + 0.5)

from decimal import Decimal
print("Decimal 精确舍入     :",
      Decimal("2.5").quantize(Decimal("1"), rounding="ROUND_HALF_UP"))   # 3
# C++: 需要自己处理或使用第三方十进制库
