from unicodedata import normalize, name

half = '½'
print(normalize('NFKC', half))
# '1⁄2'
four_squared = '4²'
print(normalize('NFKC', four_squared))
# '42'
micro = 'μ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
# ('μ', 'μ')
print(ord(micro), ord(micro_kc))
# (181, 956) 此处和原文不一样
print(name(micro), name(micro_kc))
# ('MICRO SIGN', 'GREEK SMALL LETTER MU')
