# fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
# print(sorted(fruits))
# ['acerola', 'atemoia', 'açaí', 'caju', 'cajá']

# 在linux中
import locale
locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_friuts = sorted(fruits,key = locale.strxfrm)
print(sorted_friuts)

# 操作系统必须支持区域设置，否则 setlocale 函数会抛出
# locale.Error: unsupported locale setting 异常。