# -*- coding: utf-8 -*-
"""
===============================================================================
 第 3 章  字符串与文本处理基础  ·  3.5 拼接与重复
===============================================================================
 运行方式：python 05_3.5_拼接与重复.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("3.5 拼接与重复")
print("=" * 70)

# ---- + 拼接：每次都会创建新字符串 ----
greeting = "Hello" + ", " + "World"
print(greeting)
# C++: std::string 的 operator+ 同样返回新对象

# ---- * 重复 ----
line = "-" * 20
print(line)
print("ab" * 3)            # ababab
print("ab" * 0)            # 空字符串
print("ab" * -2)           # 空字符串（负数不会报错，C++ 无此运算）
# C++: 需要 std::string(20, '-') 或循环拼接

# ---- join：把"可迭代的字符串"拼成一个（推荐做法）----
words = ["Python", "is", "fun"]
print(" ".join(words))
print(",".join(words))
# C++: 需要手写循环，注意最后一项不要多加分隔符

# join 要求元素必须都是 str，数字要先用 map(str, ...) 转换
numbers = [1, 2, 3]
print("-".join(map(str, numbers)))     # "1-2-3"
# 写成 "-".join(numbers) 会抛 TypeError: sequence item 0: expected str instance, int found

# ---- 大量拼接用 join，不要用 +=（+= 会反复创建新字符串，O(n^2)）----
parts = []
for k in range(5):
    parts.append(str(k))
print("".join(parts))       # "01234"
# C++: 同样是"先收集再拼接"更快，或使用 std::ostringstream

# 反向拼接
print("".join(reversed("abc")))        # cba
print("-".join(["a", "b"]))            # a-b
