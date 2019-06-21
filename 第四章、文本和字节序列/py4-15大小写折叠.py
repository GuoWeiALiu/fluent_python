from unicodedata import name

mirco = 'μ'
print(name(mirco))
# MICRO SIGN
micro_cf = mirco.casefold()
print(name(micro_cf))
# GREEK SMALL LETTER MU'
# 微符号 'μ' 会变成小写的希腊字母“μ”（在多数字体中二者看起来一样）；
eszett = 'ß'
print(name(eszett))
eszett_cf  = eszett.casefold()
print(eszett,eszett_cf)

# 德语 Eszett（“sharp s”，ß）会变成“ss”