open('cafe.txt', 'w', encoding='utf_8').write('café')
print(open('cafe.txt').read())
print(open('cafe.txt',encoding='utf_8').read())