class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()
    
    def reduce(self):
        for x in range(2,self.numerator + 1):
            if self.numerator % x == 0 and self.denominator % x == 0:
                self.numerator //= x
                self.denominator //= x
                return self.reduce()
        return self
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            tempFrac = Fraction(self.numerator * other.denominator + self.denominator * other.numerator,\
                self.denominator * other.denominator)
            return tempFrac
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self + tempFrac
        
    def __sub__(self,other):
        if isinstance(other, Fraction):
            tempFrac = Fraction(self.numerator * other.denominator - self.denominator * other.numerator,\
                self.denominator * other.denominator)
            return tempFrac
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self - tempFrac
    
    def __mul__(self, other):
        if isinstance(other, Fraction):
            tempFrac = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
            return tempFrac
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self * tempFrac
    
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            tempFrac = Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
            return tempFrac
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self / tempFrac
    
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self == tempFrac
        
    def __ne__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator != self.denominator * other.numerator
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self != tempFrac
    
    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < self.denominator * other.numerator
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self < tempFrac
    
    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator <= self.denominator * other.numerator
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self <= tempFrac
        
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > self.denominator * other.numerator
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self > tempFrac
    
    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator >= self.denominator * other.numerator
        if isinstance(other, int):
            tempFrac = Fraction(other,1)
            return self >= tempFrac
    
    def out(self):
        return f'{self.numerator}/{self.denominator}'

