br1 = 1/2.43
print(br1)
print(format(br1,'0.4f'))
# 格式说明符是 '0.2f'。代换字段中的 'rate' 子串是字段名称，与
# 格式说明符无关，但是它决定把 .format() 的哪个参数传给代换字
# 段。
print('1 BRL = {rate:0.2f} USD'.format(rate=br1))
# 格式规范微语言为一些内置类型提供了专用的表示代码
print(format(42,'b'))
print(format(2/3,".1%"))
from datetime import datetime
now = datetime.now()
print(format(now, "%H:%M:%S"))
print("it is now {:%I:%M:%p}".format(now))