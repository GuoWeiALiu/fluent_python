import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # ➊

        return SentenceIterator(self.words)  # ➋


class SentenceIterator:

    def __init__(self, words):
        self.words = words
        self.index = 0  # ➍

    def __next__(self):
        try:
            word = self.words[self.index]  # ➎
        except IndexError:
            raise StopIteration()  # ➏
        self.index += 1  # ➐
        return word  # ➑

    def __iter__(self):  # ➒
        return self
