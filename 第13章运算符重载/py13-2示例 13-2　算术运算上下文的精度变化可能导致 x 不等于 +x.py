import decimal
ctx = decimal.getcontext()
ctx.prec = 40
one_third = decimal.Decimal('1')/decimal.Decimal('3')
print(one_third)
print(one_third ==+one_third)
ctx.prec = 28
print(one_third)
print(one_third ==+one_third)
print(+one_third)
# 虽然每个 +one_third 表达式都会使用 one_third 的值创建一个
# 新 Decimal 实例，但是会使用当前算术运算上下文的精度。