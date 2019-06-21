city = 'São Paulo'
# ❶ 'utf_?' 编码能处理任何字符串。
print(city.encode('utf_8'))
print(city.encode('utf_16'))
# ❷ 'iso8859_1' 编码也能处理字符串 'São Paulo'。
print(city.encode('iso8859_1'))
# ❸ 'cp437' 无法编码 'ã'（带波形符的“a”）。默认的错误处理方式
# 'strict' 抛出 UnicodeEncodeError。
# print(city.encode('cp437'))
# ❹ error='ignore' 处理方式悄无声息地跳过无法编码的字符；这样做
# 通常很是不妥。
print(city.encode('cp437',errors = 'ignore'))
# ❺ 编码时指定 error='replace'，把无法编码的字符替换成 '?'；数
# 据损坏了，但是用户知道出了问题。
print(city.encode('cp437',errors = 'replace'))
# ❻ 'xmlcharrefreplace' 把无法编码的字符替换成 XML 实体
print(city.encode('cp437',errors = 'xmlcharrefreplace'))