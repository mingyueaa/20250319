# -*- coding: utf-8 -*-
"""
===============================================================================
 第 1 章  变量、数据类型与输入输出  ·  1.13 输出：print 的 sep / end / file / flush
===============================================================================
 运行方式：python 13_1.13_输出_print_的_sep_end_file_flush.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("1.13 输出：print 的 sep / end / file / flush")
print("=" * 70)

print("默认分隔符是空格:", 1, 2, 3)
# C++: std::cout << 1 << " " << 2 << " " << 3 << "\n";

print("自定义 sep:", 2026, 10, 29, sep="-")          # 2026-10-29
print("不换行:", end="")                              # end 默认是 "\n"
print("我还在同一行")
print()

# 输出到文件（file 参数）；这里写到临时文件再读出来展示
with open("_demo_print.txt", "w", encoding="utf-8") as f:
    print("写入文件的一行", file=f)
# C++: std::ofstream f("_demo_print.txt"); f << "写入文件的一行\n";
with open("_demo_print.txt", "r", encoding="utf-8") as f:
    print("从文件读回:", f.read().strip())

# 打印多个对象时，print 内部调用 str()；用 repr() 能看到更"真实"的形态
print("str('a') =", str("a"), "| repr('a') =", repr("a"))
# C++: 没有 str/repr 的区分，需要自己重载 operator<<

# 注意：C++ 的 std::endl 会刷新缓冲区；Python 的 print 默认行缓冲/块缓冲，
#       需要立即刷新可以传 flush=True。
print("立即刷新", flush=True)
