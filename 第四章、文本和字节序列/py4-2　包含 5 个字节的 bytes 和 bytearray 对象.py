# bytes 对象可以从 str 对象使用给定的编码构建。
cafe = bytes('café', encoding='utf_8')
print(cafe)
# b'caf\xc3\xa9'
# bytes 或 bytearray 对象的各个元素是介于 0~255（含）之间的整数
print(cafe[0])
# 99
# bytes 对象的切片还是 bytes 对象，即使是只有一个字节的切片。
print(cafe[:1])
# b'c'
print(cafe[0]==cafe[:1])
cafe1 = 'cafe'
print(cafe1[0]==cafe1[:1])
# bytearray 对象没有字面量句法，而是以 bytearray() 和字节序列
# 字面量参数的形式显示。
cafe_arr = bytearray(cafe)
print(cafe_arr)
# bytearray(b'caf\xc3\xa9')
print(cafe_arr[0])
# bytearray 对象的切片还是 bytearray 对象。
print(cafe_arr[:1])
# bytearray(b'c')