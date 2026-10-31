# -*- coding: utf-8 -*-
"""
===============================================================================
 第 3 章  字符串与文本处理基础  ·  3.10 实用文本处理实例
===============================================================================
 运行方式：python 10_3.10_实用文本处理实例.py
 说明：本文件是该章的一个独立小节，可单独运行，不依赖本章其他文件。
 注释约定：凡是 "# C++: ..." 都是 C++ 的对应写法或行为差异，便于对照。
===============================================================================
"""

import string
import textwrap
from collections import Counter

print("=" * 70)
print("3.10 实用文本处理实例")
print("=" * 70)

# ---- 实例 1：单词频率统计（split + dict + Counter）----
text = "the quick brown fox jumps over the lazy dog The fox"
words = text.lower().split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1      # dict.get(key, default)，第 4 章详讲
print("词频统计:", freq)

counter = Counter(words)
print("出现最多的 3 个:", counter.most_common(3))
# C++: std::unordered_map<std::string, int> 计数 + 排序

# ---- 实例 2：回文判断（清洗 + 切片反转）----
def is_palindrome(s):
    """忽略大小写、空格和标点，判断是否回文。"""
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    # C++: 遍历 + std::isalnum + std::tolower + push_back
    return cleaned == cleaned[::-1]
    # C++: return std::equal(v.begin(), v.begin() + v.size()/2, v.rbegin());

for case in ("A man, a plan, a canal: Panama", "hello", "上海自来水来自海上"):
    print(f"{case!r:<42} -> {is_palindrome(case)}")

# ---- 实例 3：清洗文本（去标点、压缩空白、统一大小写）----
dirty = "  Hello,,,   WORLD!!  This is  Python.  "
cleaned = dirty.translate(str.maketrans("", "", string.punctuation))
cleaned = " ".join(cleaned.split())        # split 无参 + join：自动压缩连续空白
cleaned = cleaned.lower()
print("\n清洗前:", repr(dirty))
print("清洗后:", repr(cleaned))

# ---- 实例 4：解析 CSV 行并转换类型 ----
line = "李雷, 20, 88.5, 北京"
fields = [f.strip() for f in line.split(",")]
p_name, p_age, p_score, p_city = fields[0], int(fields[1]), float(fields[2]), fields[3]
print(f"\n姓名={p_name}, 年龄={p_age}, 分数={p_score}, 城市={p_city}")
# C++: std::getline(ss, token, ',') + std::stoi / std::stod

# ---- 实例 5：对齐输出表格 ----
rows = [("Alice", 92, 88), ("Bob", 100, 75), ("张三", 66, 99)]
print("\n" + "-" * 36)
print(f"{'姓名':<10}{'语文':>8}{'数学':>8}{'总分':>10}")
print("-" * 36)
for nm, chinese, math_score in rows:
    print(f"{nm:<10}{chinese:>8}{math_score:>8}{chinese + math_score:>10}")
print("-" * 36)

# ---- 实例 6：简单模板替换 ----
template = "尊敬的 {name}，您本月的账单为 {amount:.2f} 元，请在 {day} 日前缴纳。"
message = template.format(name="王先生", amount=1234.5, day=15)
print("\n" + message)

# 也可以用 f-string（适合字段固定的场景）
name2, amount2, day2 = "李女士", 88.0, 5
print(f"尊敬的 {name2}，您本月的账单为 {amount2:.2f} 元，请在 {day2} 日前缴纳。")

# ---- 实例 7：提取字符串中的数字（逐字符判断）----
mixed = "abc123def45gh6"
digits_only = "".join(ch for ch in mixed if ch.isdigit())
print("\n提取数字:", digits_only, "| 求和:", sum(int(d) for d in digits_only))
# 更复杂的模式匹配请用 re 模块（正则表达式，后面章节/进阶内容）
import re
print("re.findall(r'\\d+', mixed) =", re.findall(r"\d+", mixed))   # ['123', '45', '6']

# ---- 实例 8：textwrap 处理长文本 ----
long_text = ("Python is a high-level, general-purpose programming language. "
             "Its design philosophy emphasizes code readability.")
print("\n按宽度 50 折行:")
print(textwrap.fill(long_text, width=50))

code_snippet = """
        if x > 0:
            print(x)
"""
print("去公共缩进:")
print(textwrap.dedent(code_snippet).strip())
# C++: 没有等价工具，需要自己处理

# ---- 实例 9：首字母缩写 ----
sentence = "central processing unit"
acronym = "".join(w[0].upper() for w in sentence.split())
print("\n缩写:", acronym)          # CPU
