from dis import dis

b = 6


def f1(a):
    print(a)
    global b
    b = 9
    print(b)


f1(3)
dis(f1)
# 3
# 9
#   7           0 LOAD_GLOBAL              0 (print) 加载全局名称 print。
#               2 LOAD_FAST                0 (a) 加载本地名称 a。
#               4 CALL_FUNCTION            1
#               6 POP_TOP
#
#   9           8 LOAD_CONST               1 (9)
#              10 STORE_GLOBAL             1 (b)
#
#  10          12 LOAD_GLOBAL              0 (print)
#              14 LOAD_GLOBAL              1 (b) 
#              16 CALL_FUNCTION            1
#              18 POP_TOP
#              20 LOAD_CONST               0 (None)
#              22 RETURN_VALUE