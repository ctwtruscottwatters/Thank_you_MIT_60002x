import numpy
import math

# Charles Thomas Wallace Truscott Watters

#work in progress 

"""
I love you my brother Tai, Father Mark William Watters, and Uncle Rodney. RIP Herbert Wallace Truscott (Wal Truscott)

Glad to work out Descartes two dimensional plane for ordered pairs, abscissa and ordinate

0 5
1 7
2 9
3 11
4 13
5 15
6 17
7 19
8 21
9 23
10 25
[(0, 5), (1, 7), (2, 9), (3, 11), (4, 13), (5, 15), (6, 17), (7, 19), (8, 21), (9, 23), (10, 25)]
18 18 35 18 18
                              |    .
                              |
                              |   .
                              |
                              |  .
                              |
                              | .
                              |
                              |
                              |
_________________|_________________

[Program finished]

"""
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
def printDescartesPlane(l):
    quad_I = "                  "
    quad_II ="                 |"
    axes_horizontal ="_________________|_________________"
    quad_III = "                | "
    quad_IV = "                  "
    print(len(quad_I), len(quad_II), len(axes_horizontal), len(quad_III), len(quad_IV))
    for x in range(11, 1, -1):
        print(quad_II, end=" ")
        for y in l:
           # print(x, y[1], x == y)
            if x == y[1]:
                print(quad_I[0:y[0]] + quad_I[y[0]:y[0] + 1:1].replace(' ', '.') + quad_I[y[0]:len(quad_I)], end="")
        print("\n", end="")  
    print(axes_horizontal)
    
def main():
        x = LinearEquation(2, 5, 0, 11)
        print(x)
        printDescartesPlane(x.tups)
        
        
if __name__ == "__main__": main()