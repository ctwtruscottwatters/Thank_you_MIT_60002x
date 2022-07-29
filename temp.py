# -*- coding: utf-8 -*-
"""
Thank you MIT. Charles Truscott. Chapter 12 Guttag et alia p. 239
MIT 6.0002 via edX. Thank you Eric Grimson and edX
"""
import math
def bin_search(L, e, low, high):
    if high == low:
        return L[low] == e #When the high-point and low-point are reached as each other return whether the value truly is there
    mid = (high + low) // 2 # Integer splice
    if L[mid] == e: #Did we get the answer straight away as the mid-point straight away?
        return True
    elif L[mid] > e:
        if low == mid:
            return False
        else:
            return bin_search(L, e, low, mid - 1) #Take the mid-point and insert it as the high point decrementing the check from the mid-point
    else:
        return bin_search(L, e, mid + 1, high) # Recurse the function if the value is lesser than
    
    
    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1) # Recurse the value for each x in L, if no other point is reached
        
nums = []
for x in range(0, 100 + 1, 1):
    nums.append(x)
for y in nums:
#    print("{} retains a perfect square: {}".format(y, bin_search(nums, math.sqrt(y), 0, len(nums))))
    if bin_search(nums, math.sqrt(y), 0, len(nums)) == True:
        print("{} is a perfect square. Charles Truscott Watters".format(y))