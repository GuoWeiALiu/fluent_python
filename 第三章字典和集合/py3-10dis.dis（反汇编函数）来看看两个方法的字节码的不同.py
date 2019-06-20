from dis import dis
print(dis('{1}')) # 检查 {1} 字面量背后的字节码。
#   1           0 LOAD_CONST               0 (1)
#               2 BUILD_SET                1  # 特殊的字节码 BUILD_SET 几乎完成了所有的工作。
#               4 RETURN_VALUE
# None
print(dis('set([1])'))        #set([1]) 的字节码。

#   1           0 LOAD_NAME                0 (set)  #3 种不同的操作代替了上面的# BUILD_SET：LOAD_NAME、BUILD_LIST 和 CALL_FUNCTION。
#               2 LOAD_CONST               0 (1)
#               4 BUILD_LIST               1
#               6 CALL_FUNCTION            1
#               8 RETURN_VALUE
# None