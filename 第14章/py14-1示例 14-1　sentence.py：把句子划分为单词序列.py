import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)  # ➊

    def __getitem__(self, index):
        return self.words[index]  # ➋

    def __len__(self):  # ➌

        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # ➍
# ❶ re.findall 函数返回一个字符串列表，里面的元素是正则表达式的
# 全部非重叠匹配。
# ❷ self.words 中保存的是 .findall 函数返回的结果，因此直接返回
# 指定索引位上的单词。
# ❸ 为了完善序列协议，我们实现了 __len__ 方法；不过，为了让对象
# 可以迭代，没必要实现这个方法。
# ❹ reprlib.repr 这个实用函数用于生成大型数据结构的简略字符串表
# 示形式。
s = Sentence('"The time has come," the Walrus said,')
print(s)
for word in s:
    print(word)
print(list(s))
s3 = Sentence('Pig and Pepper')
it = iter(s3)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(list(it))
print(list(iter(s3)))

