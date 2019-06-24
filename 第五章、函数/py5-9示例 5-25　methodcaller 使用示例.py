from operator import methodcaller
s = 'i love you'
upcase = methodcaller('upper')
print(upcase(s))
hiphenate = methodcaller('replace', ' ', '_')
print(hiphenate(s))