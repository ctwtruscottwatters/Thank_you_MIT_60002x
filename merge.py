# Charles Truscott Byron Bay NSW 2481 MIT Student 
# Thank you edx.org
"""

mid: 4, [2, 4, 8, 1], [7, 9, 3, 5]
mid: 2, [2, 4], [8, 1]
mid: 1, [2], [4]
[2] [4]
i: 0 j: 0
2 is less than 4, append 2
j = 0, append 4
[2, 4]
mid: 1, [8], [1]
[8] [1]
i: 0 j: 0
8 is greater than 1, append 1
i = 0, append 8
[1, 8]
[2, 4] [1, 8]
i: 0 j: 0
2 is greater than 1, append 1
i: 0 j: 1
2 is less than 8, append 2
i: 1 j: 1
4 is less than 8, append 4
j = 1, append 8
[1, 2, 4, 8]
mid: 2, [7, 9], [3, 5]
mid: 1, [7], [9]
[7] [9]
i: 0 j: 0
7 is less than 9, append 7
j = 0, append 9
[7, 9]
mid: 1, [3], [5]
[3] [5]
i: 0 j: 0
3 is less than 5, append 3
j = 0, append 5
[3, 5]
[7, 9] [3, 5]
i: 0 j: 0
7 is greater than 3, append 3
i: 0 j: 1
7 is greater than 5, append 5
i = 0, append 7
i = 1, append 9
[3, 5, 7, 9]
[1, 2, 4, 8] [3, 5, 7, 9]
i: 0 j: 0
1 is less than 3, append 1
i: 1 j: 0
2 is less than 3, append 2
i: 2 j: 0
4 is greater than 3, append 3
i: 2 j: 1
4 is less than 5, append 4
i: 3 j: 1
8 is greater than 5, append 5
i: 3 j: 2
8 is greater than 7, append 7
i: 3 j: 3
8 is less than 9, append 8
j = 3, append 9
[1, 2, 3, 4, 5, 7, 8, 9]
Final merged list: [1, 2, 3, 4, 5, 7, 8, 9]
CTW Truscott Watters MIT Student

[Program finished]


"""



def merge(left, right):
    result = []
    i, j = 0, 0
    while (i < len(left)) and (j < (len(right))):
        print("i: {} j: {}".format(i, j))
        if left[i] < right[j]:
            print("{} is less than {}, append {}".format(left[i], right[j], left[i]))
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            print("{} is greater than {}, append {}".format(left[i], right[j], right[j]))
            result.append(right[j])
            j += 1
    while (i < len(left)):
        print("i = {}, append {}".format(i, left[i]))
        result.append(left[i])
        i += 1
    while (j < len(right)):
        print("j = {}, append {}".format(j, right[j]))
        result.append(right[j])
        j += 1
    print(result)
    return result
      
      
def merge_sort(L):
    
    if len(L) >= 2:
        mid = len(L) // 2
        print("mid: {}, {}, {}".format(mid, L[:mid], L[mid:]))
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        print(left, right)
        return merge(left, right)
    else:
        return L[:]
 
def main():
    L = [2, 4, 8, 1, 7, 9, 3, 5]
    print("Final merged list: {}".format(merge_sort(L)))
    print("CTW Truscott Watters MIT Student")
    
    
if __name__ == "__main__": main()