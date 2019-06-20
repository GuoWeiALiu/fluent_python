needles = {1,2,3}
haystack = {1,2,3,4,5}
found = len(needles & haystack)
print(found)
# 不用集合
found1 = 0
for i in needles:
    if i in haystack:
        found1+=1
print(found1)

# 如果needles不是集合
found = len(set(needles)&set(haystack))
found = len(set(needles).intersection(haystack))

