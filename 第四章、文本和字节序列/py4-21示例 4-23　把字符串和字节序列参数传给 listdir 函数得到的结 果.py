import os

print(os.listdir('.'))
print(os.listdir(b'.'))

# os 模块中的所有函数、文件名或路径名参数既能
# # 使用字符串，也能使用字节序列。如果这样的函数使用字符串参数调
# # 用，该参数会使用 sys.getfilesystemencoding() 得到的编解码器
# # 自动编码，然后操作系统会使用相同的编解码器解码