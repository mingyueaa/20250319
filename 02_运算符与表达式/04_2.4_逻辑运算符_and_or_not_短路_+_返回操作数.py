# -*- coding: utf-8 -*-
"""
===============================================================================
 第 2 章  运算符与表达式  ·  2.4 逻辑运算符：and / or / not（短路 + 返回操作数）
===============================================================================
 运行方式：python 04_2.4_逻辑运算符_and_or_not_短路_+_返回操作数.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("2.4 逻辑运算符：and / or / not（短路 + 返回操作数）")
print("=" * 70)

t, f = True, False
print("t and f =", t and f)     # False
print("t or  f =", t or f)      # True
print("not t   =", not t)       # False
# C++: && || !，但 C++ 的结果一定是 bool

# ★ Python 的 and/or 返回的是"决定结果的那个操作数"，不是 bool
print("\n返回值是操作数，不是布尔值：")
print("0 or 'default'      =", repr(0 or "default"))      # 'default'
print("'Tom' and 'Jerry'   =", repr("Tom" and "Jerry"))   # 'Jerry'
print("'' or 0 or [] or None =", repr("" or 0 or [] or None))
print("1 and 2 and 3       =", 1 and 2 and 3)             # 3
# 记忆法：and 返回第一个"假值"，全真则返回最后一个；
#         or  返回第一个"真值"，全假则返回最后一个。
# C++: && 只会得到 true/false，没有这种"取默认值"的惯用法。
#       C++ 的等价写法是 name.empty() ? "匿名" : name;

# 常见惯用法：给变量设默认值
user_input = ""
name = user_input or "匿名"
print("name =", name)

# ---- 短路求值 ----
def side_effect(tag):
    print(f"    [调用了 {tag}]")
    return True

print("\n短路演示（and 遇到假就停）：")
_ = False and side_effect("A")     # 不会打印 A
print("短路演示（or 遇到真就停）：")
_ = True or side_effect("B")       # 不会打印 B
# C++: 同样是短路求值（&& ||），但结果只有 true/false

# 实用：先判空再访问属性，避免 AttributeError
text = None
if text and text.startswith("http"):
    print("是网址")
else:
    print("text 为空或不以 http 开头（没有报错，靠短路保护）")

# ---- 布尔运算与位运算不能混用 ----
# Python 的 and/or 用于逻辑；& | ^ 用于整数的位运算。
# C++ 中 && 和 & 都能"看起来"对 bool 生效，Python 里对 bool 用 & 会得到整数结果。
print("\nTrue & True =", True & True, "| True | False =", True | False)
