# -*- coding: utf-8 -*-
"""
===============================================================================
 第 3 章  字符串与文本处理基础  ·  3.11 本章易错点 & C++ -> Python 对照
===============================================================================
 运行方式：python 11_3.11_本章易错点_&_C++_-_Python_对照.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("3.11 本章易错点 & C++ -> Python 对照")
print("=" * 70)

checklist = [
    "str 不可变：s[0]='H' 报错；所有修改都返回新字符串。",
    "切片左闭右开 s[1:4] 取下标 1,2,3；越界切片不报错，索引越界才报错。",
    "负数步长可以反转：s[::-1]；C++ 要 std::reverse。",
    "Python 3 的 str 是 Unicode 字符，不是字节；len('中文') == 2。",
    "str 与 bytes 不能混用，必须 encode()/decode()。",
    "join 的元素必须全是 str，数字要先 map(str, ...)。",
    "find 找不到返回 -1；index 找不到抛 ValueError。",
    "'10' < '9' 是 True（按字典序，不是数值）。",
    "比较内容用 ==，不要用 is（短字符串驻留会骗你）。",
    "无参数 split() 会压缩空白并丢弃空串；split(' ') 不会。",
    "strip('xy') 删的是字符集合里的任意字符，不是子串 'xy'。",
    "绝对路径等含反斜杠的字面量用 r'...'；但 r 字符串不能以反斜杠结尾。",
    "读写文件请显式 encoding='utf-8'，Windows 默认编码不是 UTF-8。",
    "大量拼接用 ''.join(list)，不要循环 +=。",
]
for i, item in enumerate(checklist, 1):
    print(f"  {i}. {item}")

print("\nC++ -> Python 速查：")
mapping = [
    ("std::string s = \"hi\";",        "s = \"hi\""),
    ("s.size() / s.length()",          "len(s)"),
    ("s.substr(1, 3)",                 "s[1:4]"),
    ("std::reverse(s.begin(), s.end())", "s[::-1]"),
    ("s.find(t) != npos",              "t in s  /  s.find(t) != -1"),
    ("s.empty()",                      "not s"),
    ("std::toupper(c)",                "ch.upper()  (单个字符也是 str)"),
    ("s += t",                         "s += t  或  ''.join(parts)"),
    ("std::to_string(n)",              "str(n)"),
    ("std::stoi(s)",                   "int(s)"),
    ("printf(\"%.2f\", x)",            "f\"{x:.2f}\""),
    ("R\"(C:\\path)\"",                "r\"C:\\path\""),
    ("std::getline(ss, t, ',')",       "s.split(',')"),
    ("std::string(n, '-')",            "'-' * n"),
]
for cpp, py in mapping:
    print(f"  {cpp:<36} =>  {py}")

print("\n第 3 章结束。三章合起来覆盖了 Python 表达式的全部基础，")
print("下一站建议：第 4 章 条件与循环，第 5 章 函数，第 6 章 列表/字典等容器。")
