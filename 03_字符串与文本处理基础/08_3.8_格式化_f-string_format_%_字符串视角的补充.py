# -*- coding: utf-8 -*-
"""
===============================================================================
 第 3 章  字符串与文本处理基础  ·  3.8 格式化：f-string / format / %（字符串视角的补充）
===============================================================================
 运行方式：python 08_3.8_格式化_f-string_format_%_字符串视角的补充.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("3.8 格式化：f-string / format / %（字符串视角的补充）")
print("=" * 70)

name, age, score = "小明", 18, 95.678

# ---- 3.8.1 f-string 基础 ----
print(f"{name} 今年 {age} 岁，得分 {score}")

# 任意表达式都能放进花括号
print(f"明年 {age + 1} 岁；得分四舍五入 {round(score)}；名字长度 {len(name)}")

# ---- 3.8.2 对齐与填充 ----
# {值:[填充字符][<^>][宽度]}
print(f"[{name:<8}]")      # 左对齐，宽度 8
print(f"[{name:^8}]")      # 居中
print(f"[{name:>8}]")      # 右对齐
print(f"[{name:*^10}]")    # 用 * 填充并居中
print(f"[{name:中<8}]")    # 用中文填充（注意显示宽度问题）

# ---- 3.8.3 数字格式 ----
print(f"整数补零   : {42:05d}")
print(f"正负号     : {42:+d} / {-42:+d}")
print(f"千分位     : {1234567890:,}")
print(f"小数位数   : {score:.2f}")
print(f"百分比     : {0.8765:.1%}")
print(f"科学计数法 : {12345.678:.2e}")
print(f"二进制     : {42:b} / 八进制 {42:o} / 十六进制 {42:x} / {42:#x}")
print(f"通用格式   : {123456789.123:,.2f}")

# ---- 3.8.4 嵌套格式说明符（宽度/精度来自变量）----
width, precision = 10, 3
print(f"[{score:{width}.{precision}f}]")     # 宽度 10，保留 3 位小数

# ---- 3.8.5 调试语法 = （3.8+）----
print(f"{score = }")            # score = 95.678
print(f"{age * 2 = }")          # age * 2 = 36

# ---- 3.8.6 转换标志 !r / !s / !a ----
raw = "换行\n"
print(f"{raw!r}")               # '换行\n'
print(f"{raw!a}")               # 非 ASCII 转义成 \uXXXX

# ---- 3.8.7 str.format() ----
print("\n{}-{}-{}".format(2026, 10, 29))
print("{1}-{0}".format("A", "B"))             # B-A 按位置
print("{name} is {age}".format(name="Tom", age=20))
person = {"name": "Jerry", "age": 5}
print("{name} is {age}".format_map(person))   # 用字典填充

# ---- 3.8.8 % 旧式格式化 ----
print("\n%s 今年 %d 岁，得分 %.2f，占比 %.1f%%" % (name, age, score, 87.65))
print("%-8s|%8s" % ("左", "右"))               # 左/右对齐
print("%(name)s is %(age)d" % person)          # 用字典填充
# C++: printf("%s %d %.2f", ...) 语法几乎一样，但要注意 Python 的 %s 会自动 str()

# ---- 3.8.9 日期格式化（datetime 结合 f-string）----
from datetime import datetime
now = datetime(2026, 10, 29, 14, 30, 0)
print(f"\n{now:%Y-%m-%d %H:%M:%S}")            # 2026-10-29 14:30:00
print(f"{now:%Y年%m月%d日 %A}")                 # %A 是英文星期全名
# C++20: std::format("{:%Y-%m-%d}", ...)；C++17 需要 std::put_time
