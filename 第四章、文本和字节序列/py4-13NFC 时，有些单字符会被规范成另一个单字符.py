from unicodedata import normalize, name

ohm = '\u2126'

print(name(ohm))
# OHM SIGN
ohm_c = normalize('NFC', ohm)
print(name(ohm_c))
# GREEK CAPITAL LETTER OMEGA
print(ohm == ohm_c)
# False
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))



# True

# 电阻的单
# 位欧姆（Ω）会被规范成希腊字母大写的欧米加。这两个字符在视觉上
# 是一样的，但是比较时并不相等，因此要规范化