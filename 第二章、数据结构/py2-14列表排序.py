fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
# ['apple', 'banana', 'grape', 'raspberry']
print(fruits)
# ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits, reverse=True))
# ['raspberry', 'grape', 'banana', 'apple']
print(sorted(fruits, key=len))
# ['grape', 'apple', 'banana', 'raspberry']
print(sorted(fruits, key=len, reverse=True))
# ['raspberry', 'banana', 'grape', 'apple']
print(fruits)
# ['grape', 'raspberry', 'apple', 'banana']
print(fruits.sort())
print(fruits)
# ['apple', 'banana', 'grape', 'raspberry']