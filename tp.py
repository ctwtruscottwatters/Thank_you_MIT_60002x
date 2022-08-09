import numpy as np
import pylab

def main():
    fp = [lambda x: x ** 2, lambda x: x ** 3, lambda x: 1/x]
    my_x = []
    for x in range(1, 101):
        my_x.append(x)
    mySquares = []
    myCubes = []
    myQuotients = []
    count = 1
    for f in fp:
        for x in range(1,  100 + 1):
            if count == 1:
                mySquares.append(f(x))
            elif count == 2:
                myCubes.append(f(x))
            elif count == 3:
                myQuotients.append(f(x))
        count += 1
    pylab.plot(my_x, mySquares)
    pylab.plot(my_x, myCubes)
    pylab.plot(my_x, myQuotients)
    pylab.xlabel("x squared does not nearly grow as quickly as x cubed")
    pylab.ylabel("Zero to a million, x squared, cubed and one over x")
    pylab.title("Charles Truscott")
    pylab.show()
    pylab.savefig('three_plots1.jpg')
if __name__ == "__main__": main()