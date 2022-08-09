import numpy
import math

# Charles Thomas Wallace Truscott Watters
class OrderedPair(object):
    def __init__(self, tups):
        self.tups, tups = tups, []
    def __str__(self):
        return str(self.tups)
class LinearEquation(OrderedPair):
    def __init__(self, m, b, low, high):
        self.m = m
        self.b = b
        self.low = low
        self.high = high
        tups = []
        for x in range(low, high, 1):
            tups.append((x, self.m * x + self.b),)
            print(x, self.m * x + self.b)
        super().__init__(tups)
def main():
        x = LinearEquation(2, 5, 0, 11)
        print(x)
        
        
        
if __name__ == "__main__": main()