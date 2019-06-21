fp = open('cafe.txt', 'w', encoding='utf_8')
# ❶ 默认情况下，open 函数采用文本模式，返回一个 TextIOWrapper
# 对象。
print(fp)
# ❷ 在 TextIOWrapper 对象上调用 write 方法返回写入的 Unicode 字符
# 数。
print(fp.write('café'))
fp.close()
import os
# ❸ os.stat 报告文件中有 5 个字节；UTF-8 编码的 'é' 占两个字节，
# 0xc3 和 0xa9。
print(os.stat('cafe.txt').st_size)

fp2 = open('cafe.txt')
print(fp2)
# ❹ 打开文本文件时没有显式指定编码，返回一个 TextIOWrapper 对
# 象，编码是区域设置中的默认值。
print(fp2.encoding)
# ❺ TextIOWrapper 对象有个 encoding 属性；查看它，发现这里的编
# 码是 cp1252。
fp2.read()
# ❻ 在 Windows cp1252 编码中，0xc3 字节是“Ã”（带波形符的 A），
# 0xa9 字节是版权符号。

# ❼ 使用正确的编码打开那个文件。
fp3 = open('cafe.txt',encoding='utf_8')
print(fp3)
print(fp3.read())
# ❽ 结果符合预期：得到的是四个 Unicode 字符 'café'。
# ❾ 'rb' 标志指明在二进制模式中读取文件。
fp4 = open('cafe.txt','rb')

print(fp4)
# ❿ 返回的是 BufferedReader 对象，而不是 TextIOWrapper 对象。
print(fp4.read())
# ⓫读取返回的字节序列，结果与预期相符。