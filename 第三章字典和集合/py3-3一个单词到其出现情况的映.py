import sys
import re

WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 这其实是一种很不好的实现，这样写只是为了证明论点
            # 获取单词的出现情况列表，如果单词不存在，把单词和一个空列表
            # 放进映射，然后返回这个空列表，这样就能在不进行第二次查找的情况
            # 下更新列表了
            index.setdefault(word, []).append(location)
for word in sorted(index, key=str.upper):
    # sorted
    # 函数的
    # key = 参数没有调用
    # str.uppper，而是把这个方法
    # 的引用传递给
    # sorted
    # 函数，这样在排序的时候，单词会被规范成统一
    # 格式。
    print(word, index[word])