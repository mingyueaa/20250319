# -*- coding: utf-8 -*-
"""
===============================================================================
 第 3 章  字符串与文本处理基础  ·  3.7 常用方法一览（按功能分类）
===============================================================================
 运行方式：python 07_3.7_常用方法一览_按功能分类.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

import string

print("=" * 70)
print("3.7 常用方法一览（按功能分类）")
print("=" * 70)

sample = "  Hello Python World  "

# ---------- 3.7.1 大小写 ----------
print("原始        :", repr(sample))
print("upper()     :", sample.upper())        # 全部大写；C++: std::transform + ::toupper
print("lower()     :", sample.lower())        # 全部小写
print("capitalize():", sample.capitalize())   # 首字符大写、其余小写；不去空格，所以开头是空格时首字母不会变大写
print("title()     :", sample.title())        # 每个单词首字母大写
print("swapcase()  :", sample.swapcase())     # 大小写互换
print("casefold()  :", "Straße".casefold())   # 更彻底的小写（德语 ß -> ss）

# ---------- 3.7.2 去空白 / 去指定字符 ----------
print("\nstrip()       :", repr(sample.strip()))          # 去掉两端空白
print("lstrip()      :", repr(sample.lstrip()))         # 只去左边
print("rstrip()      :", repr(sample.rstrip()))         # 只去右边
print("strip(' x')   :", repr("xx hi xx".strip(" x")))   # 参数是"字符集合"，不是子串
print("rstrip('\\n')  :", repr("line\n".rstrip("\n")))   # 去行尾换行
# C++: 没有内置 trim，需要自己写（find_first_not_of / find_last_not_of）

# ---------- 3.7.3 查找 ----------
s = "banana"
print("\nfind('a')     :", s.find("a"))        # 1   找不到返回 -1
print("rfind('a')    :", s.rfind("a"))       # 5   从右往左找
print("find('z')     :", s.find("z"))        # -1
print("find('a', 2)  :", s.find("a", 2))     # 3   从下标 2 开始找
print("index('a')    :", s.index("a"))       # 1   找不到抛 ValueError
print("count('a')    :", s.count("a"))       # 3
print("count('an')   :", s.count("an"))      # 2   不重叠计数
# C++: find() 返回 npos 而不是 -1；没有 count 子串，需要自己循环

try:
    s.index("z")
except ValueError as e:
    print("index('z') 抛异常:", e)

# ---------- 3.7.4 判断类 ----------
print("\n'123'.isdigit()   :", "123".isdigit())      # True
print("'１２３'.isdigit()  :", "１２３".isdigit())     # True（全角数字也算）
print("'abc'.isalpha()   :", "abc".isalpha())      # True
print("'abc1'.isalnum()  :", "abc1".isalnum())     # True（字母或数字）
print("'   '.isspace()   :", "   ".isspace())      # True
print("'abc'.islower()   :", "abc".islower())      # True
print("'ABC'.isupper()   :", "ABC".isupper())      # True
print("'Hello'.istitle() :", "Hello".istitle())    # True
print("'中文'.isalpha()  :", "中文".isalpha())      # True（Unicode 字母）
# C++: <cctype> 的 isdigit/isalpha/isalnum/isspace/islower/isupper，但只对 ASCII 可靠

# ---------- 3.7.5 前后缀 ----------
url = "https://example.com/index.html"
print("\nstartswith('https') :", url.startswith("https"))
print("endswith('.html')   :", url.endswith(".html"))
print("startswith(元组)    :", url.startswith(("http://", "https://")))  # 任一匹配
# C++20: std::string::starts_with / ends_with；C++17 及之前要自己 substr 比较

# ---------- 3.7.6 分割 ----------
csv_line = "张三,18,95.5"
print("\nsplit(',')   :", csv_line.split(","))       # ['张三', '18', '95.5']
print("split(',', 1):", csv_line.split(",", 1))      # 最多切 1 次 ['张三', '18,95.5']
print("split()      :", "  a   b  c ".split())       # 无参数：按任意空白切，并丢掉空串
print("split(' ')   :", "  a   b  c ".split(" "))    # 指定空格：会保留空串
print("rsplit(',', 1):", csv_line.rsplit(",", 1))    # 从右往左切
print("splitlines() :", "a\r\nb\nc".splitlines())    # ['a', 'b', 'c']，各种换行都处理
print("partition(',') :", csv_line.partition(","))   # ('张三', ',', '18,95.5') 三段
# C++: 需要 std::getline(std::istringstream, token, ',') 或自己 find/substr

# ---------- 3.7.7 替换 ----------
print("\nreplace('a','A')      :", "banana".replace("a", "A"))       # bAnAnA
print("replace('a','A',2)    :", "banana".replace("a", "A", 2))     # bAnAna
print("replace 不改变原串     :", "banana")                          # banana
# C++: 没有直接替换子串的成员函数，需要 find + replace 循环

print("removeprefix('https://') :", url.removeprefix("https://"))    # 3.9+
print("removesuffix('.html')    :", url.removesuffix(".html"))       # 3.9+
# C++20: 类似的 starts_with 组合，或自己 substr

# ---------- 3.7.8 对齐 / 填充 ----------
print("\ncenter(20,'*') :", "标题".center(20, "*"))
print("ljust(10,'-')  :", "左".ljust(10, "-"))
print("rjust(10,'-')  :", "右".rjust(10, "-"))
print("zfill(6)       :", "42".zfill(6))      # 000042
print("zfill(6) 负数  :", "-42".zfill(6))     # -00042（符号在最前）
# C++: std::setw + std::left/std::right/std::setfill，需配合 iostream

# ---------- 3.7.9 字符映射 translate ----------
table = str.maketrans("abc", "ABC")          # a->A, b->B, c->C
print("\n'aabbcc'.translate :", "aabbcc".translate(table))    # AABBCC
delete_punct = str.maketrans("", "", string.punctuation)
print("去标点             :", "Hi, world! (test)".translate(delete_punct))
# C++: 手写循环 + std::remove_if 或 map 查表
