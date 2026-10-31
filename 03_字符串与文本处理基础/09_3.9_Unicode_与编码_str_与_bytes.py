# -*- coding: utf-8 -*-
"""
===============================================================================
 第 3 章  字符串与文本处理基础  ·  3.9 Unicode 与编码：str 与 bytes
===============================================================================
 运行方式：python 09_3.9_Unicode_与编码_str_与_bytes.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("3.9 Unicode 与编码：str 与 bytes")
print("=" * 70)

# Python 3 的 str 是"Unicode 字符序列"，内部与编码无关。
# bytes 是"字节序列"，用于文件、网络等二进制场景。
cn = "中文abc"
print("len(str)   =", len(cn))                     # 6 个字符
print("len(bytes) =", len(cn.encode("utf-8")))     # 9 个字节（每个中文 3 字节）
print("UTF-8 字节 :", cn.encode("utf-8"))           # b'\xe4\xb8\xad\xe6\x96\x87abc'
print("GBK 字节   :", cn.encode("gbk"))             # b'\xd6\xd0\xce\xc4abc'
# C++: std::string 就是字节序列，编码完全靠约定；std::u8string / std::wstring 才区分

# 解码：bytes -> str
raw = cn.encode("utf-8")
print("解码回来   :", raw.decode("utf-8"))

# 编码错误处理
try:
    "中文".encode("ascii")
except UnicodeEncodeError as e:
    print("ascii 编码失败:", str(e)[:60], "...")
print("errors='ignore' :", "中文abc".encode("ascii", errors="ignore"))   # b'abc'
print("errors='replace':", "中文abc".encode("ascii", errors="replace"))  # b'??abc'
# C++: 通常靠 iconv / std::codecvt（已弃用）/ 平台 API

# bytes 的索引得到的是"整数"，不是字符
b = b"abc"
print("\nb[0] =", b[0], "| type =", type(b[0]))     # 97 <class 'int'>
print("b[0:2] =", b[0:2])                            # b'ab'
# C++: char 本质上也是整数，表现类似

# bytes 字面量与 str 不能混用
try:
    b"abc" + "def"
except TypeError as e:
    print("b'abc' + 'def' 抛异常:", e)

# ord / chr：字符 <-> 码点
print("\nord('A') =", ord("A"))          # 65    C++: (int)'A'
print("chr(65)  =", chr(65))             # A     C++: (char)65
print("ord('中') =", ord("中"))          # 20013
print("hex(ord('中')) =", hex(ord("中")))  # 0x4e2d
print("chr(0x4e2d) =", chr(0x4E2D))
# C++: 对 ASCII 有效；Unicode 需要 std::wstring_convert / 平台 API

# 文件读写时显式指定编码（Windows 默认是 GBK，不指定容易乱码）
with open("_demo_utf8.txt", "w", encoding="utf-8") as f:
    f.write("中文内容\n")
with open("_demo_utf8.txt", "r", encoding="utf-8") as f:
    print("\n文件读回:", f.read().strip())
# C++: std::ofstream 不处理编码，写入的字节取决于源文件编码
