import sys
import re

import collections

WORD_RE = re.compile(r'\w+')
# 把 list 构造方法作为 default_factory 来创建一个defaultdict
index = collections.defaultdict(list)
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
            index[word].append(location)
            # 如果index  并没有word的记录，那么  default_factory 会被调用，为查询不到的键创造一个值。这个值在这里是一个空的列表，然后
            # 这个空列表被赋值给ndex[word]，继而被当作返回值返回，因此 .append(location)            操作总能成功。
for word in sorted(index, key=str.upper):

    print(word, index[word])