
"""
@property 就是把一个方法变成该类的属性；

该属性可以判断值，例如：学生的分数只能是整数，且在0-100之间

当 @proprtty 修饰一个函数时，它自身又创建了另一个装饰器 @函数名.setter

负责把一个setter方法变成属性复制操作，这样我们就可以操作属性的值了。

"""

class Student(object):

    _score = 0
    _birth = ''


    # score属性既有getter 又有setter，所以为可读写属性
    @property
    def score(self):  # getter方法用户获取属性值
        return self._score

    @score.setter
    def score(self, value):  # setter 方法用于修改属性的值
        if not isinstance(value, int):
            raise ValueError("score is an int number")

        if value < 0 or value > 100:
            raise ValueError("score must in 0~100!")

        self._score = value

    # birth 属性只有getter方法，所以是只读属性
    @property
    def birth(self):
        return self._birth

    @property
    def jue(self):
        jue = ''
        if self.score >= 90:
            jue = "OK"
        else:
            jue = "NO"
        return jue




s = Student()
print(s.score)
s.score = 95
print(s.score)
print(s.jue)



