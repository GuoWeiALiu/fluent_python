# 含有三个不同引用列表的列表
# list= [['_'] * 3 for i in range(3)]
# print(list)
# list[1][2]='x'
# print(list)
# 含有三个相同引用的列表
# list1 = [['_']*3]*3
# print(list1)
# list1[1][2]='x'
# print(list1)
# 和上面相同效果
row= ['_']*3
borad = []
for i in range(3):
    borad.append(row)
print(borad)
borad[1][2]="x"
print(borad)
# 和第一个相同效果
borad1=[]
for i in range(3):
    row = ['_']*3
    borad1.append(row)
print(borad1)
borad1[1][2]='x'
print(borad1)