# -*- coding: utf-8 -*-
"""
===============================================================================
 第 1 章  变量、数据类型与输入输出  ·  1.5 数据类型总览与 type() / isinstance()
===============================================================================
 运行方式：python 05_1.5_数据类型总览与_type()_isinstance().py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

print("=" * 70)
print("1.5 数据类型总览与 type() / isinstance()")
print("=" * 70)

samples = [
    42,             # int      整数（任意精度）
    3.14,           # float    双精度浮点数
    True,           # bool     布尔
    2 + 3j,         # complex  复数
    "hello",        # str      字符串（不可变）
    None,           # NoneType 空值
    [1, 2],         # list     列表（后面章节详细讲）
    (1, 2),         # tuple    元组
    {1, 2},         # set      集合
    {"k": 1},       # dict     字典
]

for value in samples:
    # type(value) 返回类型对象；.__name__ 取出类型名字符串
    print(f"{repr(value):>12}  ->  {type(value).__name__}")

# isinstance(obj, 类型) 判断对象是否属于某个类型（会考虑继承关系）
print("isinstance(42, int)      =", isinstance(42, int))
print("isinstance(True, int)    =", isinstance(True, int))    # True! bool 是 int 的子类
print("isinstance(3.0, float)   =", isinstance(3.0, float))
print("isinstance('a', (int, str)) =", isinstance("a", (int, str)))  # 可以传类型元组
# C++: typeid / dynamic_cast / std::is_same_v<...>，且都在编译期或 RTTI 层面
