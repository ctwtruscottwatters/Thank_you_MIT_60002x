import random
""" Charles Truscott Watters, Preparing for 6.0002, Coin Flip Simulation Probabilistic Model

Relative Frequency of Heads: 5059/10000 or 50.59%
Relative Frequency of Tails: 4941/10000 or 49.41%

[Program finished]
 """ 

def main():
    count = 0
    numHeads = 0
    numTails = 0
    for x in range(1, 10000 + 1, 1):
        head_or_tail = random.choice(['H','T'])
        if head_or_tail is 'H':
            numHeads += 1
        elif head_or_tail is 'T':
            numTails += 1
        count += 1
    print("Relative Frequency of Heads: {}/{} or {}%".format(numHeads, count, numHeads / count * 100))
    print("Relative Frequency of Tails: {}/{} or {}%".format(numTails, count, numTails / count * 100))
    
if __name__ == "__main__":main()