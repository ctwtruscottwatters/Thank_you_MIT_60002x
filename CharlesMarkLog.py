import math
import os

class myNum(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    pass
    
def main():
    high = 100000000
    low = 0
    guess = (high + low)/2.0
    while(round(abs((math.pi/math.sqrt(1993) * math.pi/math.sqrt(1955) * (guess/10041955) * guess/13011993 * math.sqrt(2))), 5) != round(math.log10(math.pi), 5)):
        print("guess: {} high: {} low: {}".format(guess, high, low))
        if round(abs((math.pi/math.sqrt(1993) * math.pi/math.sqrt(1955) * (guess/10041955) * guess/13011993)* math.sqrt(2)), 5)  > round(math.log10(math.pi), 5):
            high = guess
        if round(abs((math.pi/math.sqrt(1993) * math.pi/math.sqrt(1955) * (guess/10041955) * guess/13011993)* math.sqrt(2)), 5) < round(math.log10(math.pi), 5):
            low = guess
        guess = (high + low) / 2.0
              
        
    print("Final guess: {}".format(guess))
    print("Pi: {} guess:{}".format(round(10 ** math.log10(math.pi), 5), 10 ** round(abs((math.pi/math.sqrt(1993) * math.pi/math.sqrt(1955) * (guess/10041955) * guess/13011993 * math.sqrt(2))), 5)))
    print("10 ^ (Pi / (1993^(1/2)) × Pi /(1955^(1/2)) × ({}/10041955) × ({}/13011993) × (2^(1/2))) = {} (Pi)".format(guess, guess,10 ** round(abs((math.pi/math.sqrt(1993) * math.pi/math.sqrt(1955) * (guess/10041955) * guess/13011993 * math.sqrt(2))), 5)))
 
if __name__ == "__main__":main()
