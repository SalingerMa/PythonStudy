# -*- coding: utf-8 -*-

from collections import namedtuple
"""
# namedtuple 用以构建只有少数属性但是没有方法的对象，比如数据库条目。
"""


Card = namedtuple("Card", ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

suitValues = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_hight(card):
    rankValue = FrenchDeck.ranks.index(card.rank)  # 返回int类型（card在ranks中的位置）
    return rankValue * len(suitValues) + suitValues[card.suit]


from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector(%r, %r)" % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(self.x or self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

from bisect import bisect

def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    index = bisect(breakpoints, score)
    return grades[index]




if __name__ == '__main__':
    grades = [grade(score) for score in [67, 45, 90, 87, 70]]
    print(grades)