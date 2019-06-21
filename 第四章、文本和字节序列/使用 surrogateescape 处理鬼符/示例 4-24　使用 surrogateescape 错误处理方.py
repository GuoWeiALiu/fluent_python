import os
# ➊ 列出目录里的文件，有个文件名中包含非 ASCII 字符。
print(os.listdir('.'))
# ➋ 假设我们不知道编码，获取文件名的字节序列形式。
print(os.listdir(b'.'))
# ➌ pi_names_bytes 是包含 π 的文件名。
pi_name_bytes = os.listdir(b'.')[1]
# 使用'ascii' 编解码器和 'surrogateescape' 错误处理方式把它解码成字符串。
pi_name_str = pi_name_bytes.decode('ascii','surrogateescpe')
# ➎ 各个非 ASCII 字节替换成代替码位：'\xcf\x80' 变成
# 了'\udccf\udc80'
print(pi_name_str)
# 'digits-of-\udccf\udc80.txt'
# ➏ 编码成 ASCII 字节序列：各个代替码位还原成被替换的字节。
print(pi_name_str.encode('ascii', 'surrogateescape'))
# b'digits-of-\xcf\x80.txt