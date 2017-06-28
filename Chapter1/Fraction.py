
class Fraction:
    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den);

    def __add__(self, otherFraction):
        newNum = self.num * otherFraction.dem + self.den * otherFraction.num
        newDen = self.den * otherFraction.den

        return Fraction(newNum, newDen)

    def gcd(self, m, n):

        while m % n != 0:
            oldm = m
            m = n
            n = oldm % m
        return n