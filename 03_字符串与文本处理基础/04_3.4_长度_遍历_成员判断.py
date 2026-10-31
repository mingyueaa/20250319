# -*- coding: utf-8 -*-
"""
===============================================================================
 第 3 章  字符串与文本处理基础  ·  3.4 长度、遍历、成员判断
===============================================================================
 运行方式：python 04_3.4_长度_遍历_成员判断.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("3.4 长度、遍历、成员判断")
print("=" * 70)

word = "Python"
print("len(word) =", len(word))
# C++: word.size() / word.length()

# 直接遍历得到字符
print("逐字符遍历:")
for ch in word:
    print(ch, end="-")
print()

# 需要下标时用 enumerate（C++ 只能手写索引变量）
print("带下标遍历:")
for i, ch in enumerate(word):
    print(f"  {i}:{ch}", end="")
print()

# 反向遍历
for ch in reversed(word):
    print(ch, end="")
print()

# 成员判断：判断"子串"，不是"字符集合"
print("\n'th' in word      :", "th" in word)        # True
print("'z' in word       :", "z" in word)         # False
print("'z' not in word   :", "z" not in word)     # True
# C++: word.find("th") != std::string::npos
