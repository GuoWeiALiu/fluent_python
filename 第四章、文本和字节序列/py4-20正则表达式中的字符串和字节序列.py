import re
# ❶ 前两个正则表达式是字符串类型。
re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
# ❷ 后两个正则表达式是字节序列类型。
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')
# ❸ 要搜索的 Unicode 文本，包括 1729 的泰米尔数字（逻辑行直到右括
# 号才结束）。
text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
            " as 1729 = 1³ + 12³ = 9³ + 10³.")
# ❹ 这个字符串在编译时与前一个拼接起来
text_bytes = text_str.encode('utf_8')
# ❺ 字节序列只能用字节序列正则表达式搜索。

print('Text', repr(text_str), sep='\n ')
print('Numbers')
# ❻ 字符串模式 r'\d+' 能匹配泰米尔数字和 ASCII 数字。
print(' str :', re_numbers_str.findall(text_str))
# ❼ 字节序列模式 rb'\d+' 只能匹配 ASCII 字节中的数字。
print(' bytes:', re_numbers_bytes.findall(text_bytes))
print('Words')
# ❽ 字符串模式 r'\w+' 能匹配字母、上标、泰米尔数字和 ASCII 数字。
print(' str :', re_words_str.findall(text_str))
# ❾ 字节序列模式 rb'\w+' 只能匹配 ASCII 字节中的字母和数字。
print(' bytes:', re_words_bytes.findall(text_bytes))