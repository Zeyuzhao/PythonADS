def gcd(m, n):
    while m % n != 0:
        oldm = m
        m = n
        n = oldm % m
    return n

class Fraction:
    def __init__(self, top = 1, bottom = 1):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den);

    def __add__(self, otherFraction):
        newNum = self.num * otherFraction.den + self.den * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum // common, newDen // common)

    def __eq__(self, other):
        firstNum = self.num * other.den
        secNum = self.den * other.num
        return firstNum == secNum
    def __mul__(self, other):
        newNum = self.num * other.num
        newDen = self.den * other.den
        return Fraction(newNum, newDen)
    def __truediv__(self, other):
        newNum = self.num * other.den
        newDen = self.den * other.num
        return Fraction(newNum, newDen)
    

x = Fraction(1, 2)
y = Fraction(2, 3)

print(x + y)
print(x == y)
print(x * y)
print(x / y)