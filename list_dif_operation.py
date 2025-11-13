"""lst = lst + 76 # сложение каждого числа списка с определенным числом
lst = 6.5 + lst # сложение каждого числа списка с определенным числом
lst += 76.7  # сложение каждого числа списка с определенным числом
lst = lst - 76 # вычитание из каждого числа списка определенного числа
lst = 7.0 - lst # вычитание из числа каждого числа списка
lst -= 76.3
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
lst *= 5.54
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
lst = 3 / lst # деление числа на каждый элемент списка
lst /= 13.0"""

class ListMath:
    def __init__(self, arg=[]):
        self.lst_math = [i for i in arg if type(i) in (int, float)]

    def do(self, fn_name, other, new=True):
        result = [getattr(i, fn_name)(other) for i in self.lst_math]
        if new:
            return ListMath(result)
        else:
            self.lst_math = result
            return self

    def __add__(self, other):
        return self.do('__add__', other)

    def __sub__(self, other):
        return self.do('__sub__', other)

    def __rsub__(self, other):
        return self.do('__rsub__', other)

    def __mul__(self, other):
        return self.do('__mul__', other)

    def __rmul__(self, other):
        return self.do('__rmul__', other)

    def __truediv__(self, other):
        return self.do('__truediv__', other)

    def __iadd__(self, other):
        return self.do('__add__', other, False)

    def __isub__(self, other):
        return self.do('__sub__', other, False)

    def __imul__(self, other):
        return self.do('__mul__', other, False)

    def __idiv__(self, other):
        return self.do('__truediv__', other, False)