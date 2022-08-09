import random
import math as m
import numpy as np

"""
The dice was rolled 100000 times.
Relative Frequencies: 16466 rolls of one         16745 rolls of two      16856 rolls of three       16563 rolls of four     16521 rolls of five     16849 rolls of six
16.466% Ones 16.744999999999997% Twos 16.855999999999998% Threes 16.563% Fours 16.521% Fives 16.849% Sixes

[Program finished]
"""
# Charles Truscott Watters
# Byron Bay NSW Australia
def main():
    count = 0
    Rolls_of_One = 0
    Rolls_of_Two = 0
    Rolls_of_Three = 0
    Rolls_of_Four = 0
    Rolls_of_Five = 0
    Rolls_of_Six = 0
    for x in range(100000):
        choice = str(random.randint(1, 6))
#        print(choice)
        if choice == "1":
            Rolls_of_One += 1
        elif choice == "2":
            Rolls_of_Two += 1
        elif choice == "3":
            Rolls_of_Three += 1
        elif choice == "4":
            Rolls_of_Four += 1
        elif choice == "5":
            Rolls_of_Five += 1
        elif choice == "6":
            Rolls_of_Six += 1
        count += 1
    print("The dice was rolled {} times. ".format(count))
    print("Relative Frequencies: {} rolls of one \t {} rolls of two \t {} rolls of three \t {} rolls of four \t {} rolls of five \t {} rolls of six\n".format(Rolls_of_One, Rolls_of_Two, Rolls_of_Three, Rolls_of_Four, Rolls_of_Five, Rolls_of_Six))
    print("{}% Ones {}% Twos {}% Threes {}% Fours {}% Fives {}% Sixes".format(Rolls_of_One / count * 100, Rolls_of_Two / count * 100, Rolls_of_Three / count * 100, Rolls_of_Four / count * 100,  Rolls_of_Five / count * 100, Rolls_of_Six / count * 100))
    
if __name__ == "__main__": main()