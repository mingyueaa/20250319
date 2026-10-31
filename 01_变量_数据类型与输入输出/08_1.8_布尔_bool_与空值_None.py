# -*- coding: utf-8 -*-
"""
===============================================================================
 第 1 章  变量、数据类型与输入输出  ·  1.8 布尔 bool 与空值 None
===============================================================================
 运行方式：python 08_1.8_布尔_bool_与空值_None.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("1.8 布尔 bool 与空值 None")
print("=" * 70)

yes, no = True, False
# C++: true / false（小写）

print("True == 1 ?", True == 1)          # True
print("False == 0 ?", False == 0)        # True
print("True + True =", True + True)      # 2，bool 本质上是 int 的子类
print("type(True) =", type(True), "| isinstance(True, int) =", isinstance(True, int))

# 哪些值会被当作"假"？见第 2 章"真值性"。
print("bool(0) =", bool(0), "| bool('') =", bool(""), "| bool([]) =", bool([]))

# None：表示"没有值"，是 NoneType 的唯一实例（单例）
result = None
print("result is None ?", result is None)    # 判断 None 永远用 is，不要用 ==
# C++: nullptr（指针空）/ std::nullopt（optional 无值）。Python 的 None 更像"空值对象"
#      C++ 的 void 函数没有返回值，Python 函数没写 return 时默认返回 None。

# bool 参与运算时会被当成 0/1
print("True * 10 =", True * 10)              # 10
