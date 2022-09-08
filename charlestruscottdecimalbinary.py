
import numpy
import pandas
import scipy
import sklearn
# Thank you Massachusetts Institute of Technology, QS globally ranked #1 Higher Education Institution
# Charles Truscott Watters, Byron Bay NSW 2481
# 30th birthday on the 13th of January 2023
# And in just under five weeks I start six-triple-zero-two 6.0002 or 6.002x undergrad
# would be stoked to hold an MIT XSeries (via edX) certificate of Computational Thinking in Python

def return_binary_recur(radice_recur, x=63, n=2, binstr=""):
    print("radice: {} x: {} n: {} binstr: {}".format(radice_recur, x, 2, binstr))
    temp = radice_recur
    if temp == 1:
        binstr += str(1)
        print(binstr)
        return binstr
    elif temp == 0:
        binstr += str(0)
        print(binstr)
        return binstr
    if temp // (n ** x) == 1:
        binstr += str(1)
        temp -= (n ** x)
        return_binary_recur(temp, x - 1, 2, binstr)
    else:
        binstr += str(0)
        return_binary_recur(temp, x - 1, 2, binstr)
    if x == 1:
        return binstr
def return_binary_iter(radice):
    n = 2
    binstr = str("")
    for x in range(63, 1, -1):
        print("n: {} x: {} n ** x: {} radice: {}; radice // n ** x: {}".format(n, x, n ** x, radice, radice // (n ** x)))
        if radice // (n ** x) == 1 and radice != 0:
            binstr += str(1)
            radice -= (n ** x)
        else:
            binstr += str(0)
    if radice == 1:
        binstr += str(1)
        radice -= 1
    else:
        binstr += str(0)
    print(binstr)
    return binstr
def return_binary(integer_n):
    binary_string = ""
    if integer_n // 9223372036854775808 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 9223372036854775808
    else:
        binary_string += str(0)
    if integer_n // 4611686018427387904 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4611686018427387904
    else:
        binary_string += str(0)
    if integer_n // 2305843009213693952 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2305843009213693952
    else:
        binary_string += str(0)
    if integer_n // 1152921504606846976 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1152921504606846976
    else:
        binary_string += str(0)
    if integer_n // 576460752303423488 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 576460752303423488
    else:
        binary_string += str(0)
    if integer_n // 288230376151711744 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 288230376151711744
    else:
        binary_string += str(0)
    # 2 ^ 58
    if integer_n // 144115188075855872 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 144115188075855872
    else:
        binary_string += str(0)
    if integer_n // 72057594037927936 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 72057594037927936
    else:
        binary_string += str(0)
    if integer_n // 36028797018963968 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 36028797018963968
    else:
        binary_string += str(0)
    if integer_n // 18014398509481984 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 18014398509481984
    else:
        binary_string += str(0)
    if integer_n // 9007199254740992 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 9007199254740992
    else:
        binary_string += str(0)
    if integer_n // 4503599627370496 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4503599627370496
    else:
        binary_string += str(0)
    if integer_n // 2251799813685248 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2251799813685248
    else:
        binary_string += str(0)
    if integer_n // 1125899906842624 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1125899906842624
    else:
        binary_string += str(0)
    if integer_n // 562949953421312 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 562949953421312
    else:
        binary_string += str(0)
    if integer_n // 281474976710656 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 281474976710656
    else:
        binary_string += str(0)
    if integer_n // 140737488355328 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 140737488355328
    else:
        binary_string += str(0)
    if integer_n // 70368744177664 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 70368744177664
    else:
        binary_string += str(0)
    if integer_n // 35184372088832 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 35184372088832
    else:
        binary_string += str(0)
    if integer_n // 17592186044416 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 17592186044416
    else:
        binary_string += str(0)
    if integer_n // 8796093022208 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8796093022208
    else:
        binary_string += str(0)
    if integer_n // 4398046511104 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4398046511104
    else:
        binary_string += str(0)
    if integer_n // 2199023255552 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2199023255552
    else:
        binary_string += str(0)
    if integer_n // 1099511627776 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1099511627776
    else:
        binary_string += str(0)
    if integer_n // 549755813888 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 549755813888
    else:
        binary_string += str(0)
    if integer_n // 274877906944 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 274877906944
    else:
        binary_string += str(0)
    if integer_n // 137438953472 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 137438953472
    else:
        binary_string += str(0)
    if integer_n // 68719476736 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 68719476736
    else:
        binary_string += str(0)
    if integer_n // 34359738368 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 34359738368
    else:
        binary_string += str(0)
    if integer_n // 8589934592 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8589934592
    else:
        binary_string += str(0)
    if integer_n // 8589934592 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8589934592
    else:
        binary_string += str(0)
    if integer_n // 4294967296 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4294967296
    else:
        binary_string += str(0)
    if integer_n // 2147483648 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2147483648
    else:
        binary_string += str(0)
    if integer_n // 1073741824 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1073741824
    else:
        binary_string += str(0)
    if integer_n // 536870912 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 536870912
    else:
        binary_string += str(0)
    if integer_n // 268435456 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 268435456
    else:
        binary_string += str(0)
    if integer_n // 134217728 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 134217728
    else:
        binary_string += str(0)
    if integer_n // 67108864 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 67108864
    else:
        binary_string += str(0)
    if integer_n // 33554432 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 33554432
    else:
        binary_string += str(0)
    if integer_n // 16777216 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 16777216
    else:
        binary_string += str(0)
    if integer_n // 8388608 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8388608
    else:
        binary_string += str(0)
    if integer_n // 4194304 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4194304
    else:
        binary_string += str(0)
    if integer_n // 2097152 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2097152
    else:
        binary_string += str(0)
    if integer_n // 1048576 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1048576
    else:
        binary_string += str(0)
    if integer_n // 524288 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 524288
    else:
        binary_string += str(0)
    if integer_n // 262144 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 262144
    else:
        binary_string += str(0)
    if integer_n // 131072 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 131072
    else:
        binary_string += str(0)
    if integer_n // 65536 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 65536
    else:
        binary_string += str(0)
    if integer_n // 32768 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 32768
    else:
        binary_string += str(0)
    if integer_n // 16384 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 16384
    else:
        binary_string += str(0)
    if integer_n // 8192 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8192
    else:
        binary_string += str(0)
    if integer_n // 4096 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4096
    else:
        binary_string += str(0)
    if integer_n // 2048 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2048
    else:
        binary_string += str(0)
    if integer_n // 1024 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 1024
    else:
        binary_string += str(0)
    if integer_n // 512 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 512
    else:
        binary_string += str(0)
    if integer_n // 256 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 256
    else:
        binary_string += str(0)
    if integer_n // 128 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 128
    else:
        binary_string += str(0)
    if integer_n // 64 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 64
    else:
        binary_string += str(0)
    if integer_n // 32 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 32
    else:
        binary_string += str(0)
    if integer_n // 16 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 16
    else:
        binary_string += str(0)
    if integer_n // 8 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 8
    else:
        binary_string += str(0)
    if integer_n // 4 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 4
    else:
        binary_string += str(0)
    if integer_n // 2 == 1 and integer_n != 0:
        binary_string += str(1)
        integer_n -= 2
    else:
        binary_string += str(0)
    if integer_n == 1:
        binary_string += str(1)
    else:
        binary_string += str(0)

    print(binary_string[::])

def main():
#    return_binary(93)
#    print("\n")
#    return_binary(9324815590)
    print("9324815590 in binary is: {} ".format(return_binary_iter(9324815590)))
    print("I love MIT. 100% qualified and certified and bonafide MIT certificate holder in Python")
    print("Charles Truscott Watters. Byron Bay NSW 2481")
    print("248124812481 in binary is: ")
    return_binary_recur(2481248124812481, 63, 2, "")
    """
    ‭1000 1101 0000 1010 1110 1001 1001 0001 0100 0011 1100 1100 0001‬
   0000000000000000000000000000000000000000000000000000000001011101


0000000000000000101010101010110010101010101010101010101010101010
The thread 'MainThread' (0x1) has exited with code 0 (0x0).
The program 'python.exe' has exited with code 0 (0x0).
"""
"""
0000000000000000000000000000000000000000000000000000000001011101


0000000000000000000000000000010000101011110011010110010011100110
n: 2 x: 63 n ** x: 9223372036854775808 radice: 9324815590; radice // n ** x: 0
n: 2 x: 62 n ** x: 4611686018427387904 radice: 9324815590; radice // n ** x: 0
n: 2 x: 61 n ** x: 2305843009213693952 radice: 9324815590; radice // n ** x: 0
n: 2 x: 60 n ** x: 1152921504606846976 radice: 9324815590; radice // n ** x: 0
n: 2 x: 59 n ** x: 576460752303423488 radice: 9324815590; radice // n ** x: 0
n: 2 x: 58 n ** x: 288230376151711744 radice: 9324815590; radice // n ** x: 0
n: 2 x: 57 n ** x: 144115188075855872 radice: 9324815590; radice // n ** x: 0
n: 2 x: 56 n ** x: 72057594037927936 radice: 9324815590; radice // n ** x: 0
n: 2 x: 55 n ** x: 36028797018963968 radice: 9324815590; radice // n ** x: 0
n: 2 x: 54 n ** x: 18014398509481984 radice: 9324815590; radice // n ** x: 0
n: 2 x: 53 n ** x: 9007199254740992 radice: 9324815590; radice // n ** x: 0
n: 2 x: 52 n ** x: 4503599627370496 radice: 9324815590; radice // n ** x: 0
n: 2 x: 51 n ** x: 2251799813685248 radice: 9324815590; radice // n ** x: 0
n: 2 x: 50 n ** x: 1125899906842624 radice: 9324815590; radice // n ** x: 0
n: 2 x: 49 n ** x: 562949953421312 radice: 9324815590; radice // n ** x: 0
n: 2 x: 48 n ** x: 281474976710656 radice: 9324815590; radice // n ** x: 0
n: 2 x: 47 n ** x: 140737488355328 radice: 9324815590; radice // n ** x: 0
n: 2 x: 46 n ** x: 70368744177664 radice: 9324815590; radice // n ** x: 0
n: 2 x: 45 n ** x: 35184372088832 radice: 9324815590; radice // n ** x: 0
n: 2 x: 44 n ** x: 17592186044416 radice: 9324815590; radice // n ** x: 0
n: 2 x: 43 n ** x: 8796093022208 radice: 9324815590; radice // n ** x: 0
n: 2 x: 42 n ** x: 4398046511104 radice: 9324815590; radice // n ** x: 0
n: 2 x: 41 n ** x: 2199023255552 radice: 9324815590; radice // n ** x: 0
n: 2 x: 40 n ** x: 1099511627776 radice: 9324815590; radice // n ** x: 0
n: 2 x: 39 n ** x: 549755813888 radice: 9324815590; radice // n ** x: 0
n: 2 x: 38 n ** x: 274877906944 radice: 9324815590; radice // n ** x: 0
n: 2 x: 37 n ** x: 137438953472 radice: 9324815590; radice // n ** x: 0
n: 2 x: 36 n ** x: 68719476736 radice: 9324815590; radice // n ** x: 0
n: 2 x: 35 n ** x: 34359738368 radice: 9324815590; radice // n ** x: 0
n: 2 x: 34 n ** x: 17179869184 radice: 9324815590; radice // n ** x: 0
n: 2 x: 33 n ** x: 8589934592 radice: 9324815590; radice // n ** x: 1
n: 2 x: 32 n ** x: 4294967296 radice: 734880998; radice // n ** x: 0
n: 2 x: 31 n ** x: 2147483648 radice: 734880998; radice // n ** x: 0
n: 2 x: 30 n ** x: 1073741824 radice: 734880998; radice // n ** x: 0
n: 2 x: 29 n ** x: 536870912 radice: 734880998; radice // n ** x: 1
n: 2 x: 28 n ** x: 268435456 radice: 198010086; radice // n ** x: 0
n: 2 x: 27 n ** x: 134217728 radice: 198010086; radice // n ** x: 1
n: 2 x: 26 n ** x: 67108864 radice: 63792358; radice // n ** x: 0
n: 2 x: 25 n ** x: 33554432 radice: 63792358; radice // n ** x: 1
n: 2 x: 24 n ** x: 16777216 radice: 30237926; radice // n ** x: 1
n: 2 x: 23 n ** x: 8388608 radice: 13460710; radice // n ** x: 1
n: 2 x: 22 n ** x: 4194304 radice: 5072102; radice // n ** x: 1
n: 2 x: 21 n ** x: 2097152 radice: 877798; radice // n ** x: 0
n: 2 x: 20 n ** x: 1048576 radice: 877798; radice // n ** x: 0
n: 2 x: 19 n ** x: 524288 radice: 877798; radice // n ** x: 1
n: 2 x: 18 n ** x: 262144 radice: 353510; radice // n ** x: 1
n: 2 x: 17 n ** x: 131072 radice: 91366; radice // n ** x: 0
n: 2 x: 16 n ** x: 65536 radice: 91366; radice // n ** x: 1
n: 2 x: 15 n ** x: 32768 radice: 25830; radice // n ** x: 0
n: 2 x: 14 n ** x: 16384 radice: 25830; radice // n ** x: 1
n: 2 x: 13 n ** x: 8192 radice: 9446; radice // n ** x: 1
n: 2 x: 12 n ** x: 4096 radice: 1254; radice // n ** x: 0
n: 2 x: 11 n ** x: 2048 radice: 1254; radice // n ** x: 0
n: 2 x: 10 n ** x: 1024 radice: 1254; radice // n ** x: 1
n: 2 x: 9 n ** x: 512 radice: 230; radice // n ** x: 0
n: 2 x: 8 n ** x: 256 radice: 230; radice // n ** x: 0
n: 2 x: 7 n ** x: 128 radice: 230; radice // n ** x: 1
n: 2 x: 6 n ** x: 64 radice: 102; radice // n ** x: 1
n: 2 x: 5 n ** x: 32 radice: 38; radice // n ** x: 1
n: 2 x: 4 n ** x: 16 radice: 6; radice // n ** x: 0
n: 2 x: 3 n ** x: 8 radice: 6; radice // n ** x: 0
n: 2 x: 2 n ** x: 4 radice: 6; radice // n ** x: 1
000000000000000000000000000000100010101111001101011001001110010
9324815590 in binary is: 000000000000000000000000000000100010101111001101011001001110010
I love MIT. 100% qualified and certified and bonafide MIT certificate holder in Python
Charles Truscott Watters. Byron Bay NSW 2481
248124812481 in binary is:
radice: 2481248124812481 x: 63 n: 2 binstr:
radice: 2481248124812481 x: 62 n: 2 binstr: 0
radice: 2481248124812481 x: 61 n: 2 binstr: 00
radice: 2481248124812481 x: 60 n: 2 binstr: 000
radice: 2481248124812481 x: 59 n: 2 binstr: 0000
radice: 2481248124812481 x: 58 n: 2 binstr: 00000
radice: 2481248124812481 x: 57 n: 2 binstr: 000000
radice: 2481248124812481 x: 56 n: 2 binstr: 0000000
radice: 2481248124812481 x: 55 n: 2 binstr: 00000000
radice: 2481248124812481 x: 54 n: 2 binstr: 000000000
radice: 2481248124812481 x: 53 n: 2 binstr: 0000000000
radice: 2481248124812481 x: 52 n: 2 binstr: 00000000000
radice: 2481248124812481 x: 51 n: 2 binstr: 000000000000
radice: 229448311127233 x: 50 n: 2 binstr: 0000000000001
radice: 229448311127233 x: 49 n: 2 binstr: 00000000000010
radice: 229448311127233 x: 48 n: 2 binstr: 000000000000100
radice: 229448311127233 x: 47 n: 2 binstr: 0000000000001000
radice: 88710822771905 x: 46 n: 2 binstr: 00000000000010001
radice: 18342078594241 x: 45 n: 2 binstr: 000000000000100011
radice: 18342078594241 x: 44 n: 2 binstr: 0000000000001000110
radice: 749892549825 x: 43 n: 2 binstr: 00000000000010001101
radice: 749892549825 x: 42 n: 2 binstr: 000000000000100011010
radice: 749892549825 x: 41 n: 2 binstr: 0000000000001000110100
radice: 749892549825 x: 40 n: 2 binstr: 00000000000010001101000
radice: 749892549825 x: 39 n: 2 binstr: 000000000000100011010000
radice: 200136735937 x: 38 n: 2 binstr: 0000000000001000110100001
radice: 200136735937 x: 37 n: 2 binstr: 00000000000010001101000010
radice: 62697782465 x: 36 n: 2 binstr: 000000000000100011010000101
radice: 62697782465 x: 35 n: 2 binstr: 0000000000001000110100001010
radice: 28338044097 x: 34 n: 2 binstr: 00000000000010001101000010101
radice: 11158174913 x: 33 n: 2 binstr: 000000000000100011010000101011
radice: 2568240321 x: 32 n: 2 binstr: 0000000000001000110100001010111
radice: 2568240321 x: 31 n: 2 binstr: 00000000000010001101000010101110
radice: 420756673 x: 30 n: 2 binstr: 000000000000100011010000101011101
radice: 420756673 x: 29 n: 2 binstr: 0000000000001000110100001010111010
radice: 420756673 x: 28 n: 2 binstr: 00000000000010001101000010101110100
radice: 152321217 x: 27 n: 2 binstr: 000000000000100011010000101011101001
radice: 18103489 x: 26 n: 2 binstr: 0000000000001000110100001010111010011
radice: 18103489 x: 25 n: 2 binstr: 00000000000010001101000010101110100110
radice: 18103489 x: 24 n: 2 binstr: 000000000000100011010000101011101001100
radice: 1326273 x: 23 n: 2 binstr: 0000000000001000110100001010111010011001
radice: 1326273 x: 22 n: 2 binstr: 00000000000010001101000010101110100110010
radice: 1326273 x: 21 n: 2 binstr: 000000000000100011010000101011101001100100
radice: 1326273 x: 20 n: 2 binstr: 0000000000001000110100001010111010011001000
radice: 277697 x: 19 n: 2 binstr: 00000000000010001101000010101110100110010001
radice: 277697 x: 18 n: 2 binstr: 000000000000100011010000101011101001100100010
radice: 15553 x: 17 n: 2 binstr: 0000000000001000110100001010111010011001000101
radice: 15553 x: 16 n: 2 binstr: 00000000000010001101000010101110100110010001010
radice: 15553 x: 15 n: 2 binstr: 000000000000100011010000101011101001100100010100
radice: 15553 x: 14 n: 2 binstr: 0000000000001000110100001010111010011001000101000
radice: 15553 x: 13 n: 2 binstr: 00000000000010001101000010101110100110010001010000
radice: 7361 x: 12 n: 2 binstr: 000000000000100011010000101011101001100100010100001
radice: 3265 x: 11 n: 2 binstr: 0000000000001000110100001010111010011001000101000011
radice: 1217 x: 10 n: 2 binstr: 00000000000010001101000010101110100110010001010000111
radice: 193 x: 9 n: 2 binstr: 000000000000100011010000101011101001100100010100001111
radice: 193 x: 8 n: 2 binstr: 0000000000001000110100001010111010011001000101000011110
radice: 193 x: 7 n: 2 binstr: 00000000000010001101000010101110100110010001010000111100
radice: 65 x: 6 n: 2 binstr: 000000000000100011010000101011101001100100010100001111001
radice: 1 x: 5 n: 2 binstr: 0000000000001000110100001010111010011001000101000011110011
00000000000010001101000010101110100110010001010000111100111
"""
if __name__ == "__main__":main()
