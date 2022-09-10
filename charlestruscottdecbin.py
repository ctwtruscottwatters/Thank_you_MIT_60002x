
import numpy
import pandas
import scipy
import sklearn
# Thank you Massachusetts Institute of Technology,\n QS globally ranked #1 Higher Education Institution
# Charles Thomas Wallace Truscott Watters
# 10/09/2022 3:12 a.m.,  just under five weeks until 6.0002 to become an MIT alumni from an edX XSeries `Computational Thinking` certificate from MIT
# I love you Tai, Kerri and Mark
# Byron Bay NSW 2481
# Educated at Byron Bay High School, TAFE NSW, Offensive Security, SCU 
# and ultimately via edX at the Massachusetts Institute of Technology
# At Byron High I gained my School Certificate (NSW), in 2015 completing an Offensive Security Certified Professional, two years later attending SCU Gold Coast for Biomedical Science and three years after that attending SCU for Foundation Mathematics, that included most invaluably secondary to higher mathematics and rearranging and solving equations (Newton's Law of Cooling, quadratic theorem, factoring, completing the square) and next carrying on from Offensive Security I gained a certificate of completion in Python from TAFE NSW 
# and now I hold a certificate in Python from MIT, with fingers crossed to pass the capstone data science unit to earn the certificate of `Computational Thinking in Python` from Massachusetts Institute of Technology
# If I ever get an Australian Passport issued to travel or migrate either need to obtain my 1999 passport in which I visit California, Santa Monica and Hawaii, or dig up my Byron Primary reports to (under AU law) confirm I have lived my entire life in Australia
# Been on computers science dial up and Windows 95 in 1997 using Linknet, Byron Bay's first Internet Service Provider. didnt get ADSL1 until roughly 2004'
"""
Charles Thomas Wallace Truscott Watters, student at MIT.

Massachusetts Institute of Technology. QS globally #1 ranked college
Using recursion, 248124812481 in binary is:
00000000000000000000000000111001110001010110010000101100111
Using iteration, 248124812481 in hexadecimal is: 39C5642CC1
Using iteration, 10041955 in binary is: 0000000000000000000000000000000000000000100110010011101001100011
15 and 255 in hex and binary are:

F and 0000000000000000000000000000000000000000000000000000000000001111

and FF and 0000000000000000000000000000000000000000000000000000000011111111

[Program finished]
"""
def return_hexadecimal_iter(number):
    """ DOCSTRING: Inputs an integer and outputs a quadword. One parameter for an integer to return a quadword for. Charles Thomas Wallace Truscott Watters, Byron Bay NSW 2481 """
    hexstr = ""
    n = 16
    for x in range(16, 0, -1):
        for y in range(15, 0, -1):
#            print("x: {} y: {} number: {} hexstr: {}".format(x, y, number, hexstr))
#            print("number // y * n ** x: {} ".format(number // (y * (n ** x))))
            if number // (y * (n ** x)) == 1 and y == 15:
                hexstr += "F"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 14:
                hexstr += "E"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 13:
                hexstr += "D"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 12:
                hexstr += "C"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 11:
                hexstr += "B"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 10:
                hexstr += "A"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 9:
                hexstr += "9"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 8:
                hexstr += "8"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 7:
                hexstr += "7"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 6:
                hexstr += "6"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 5:
                hexstr += "5"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 4:
                hexstr += "4"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 3:
                hexstr += "3"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 2:
                hexstr += "2"
                number -= (y * (n ** x))
                break
            elif number // (y * (n ** x)) == 1 and y == 1:
                hexstr += "1"
                number -= (y * (n ** x))
                break
#    print(number)
    if number // 15 == 1:
        hexstr += "F"
        number -= 15
    elif number // 14 == 1:
        hexstr += "E"
        number -= 14
    elif number // 13 == 1:
        hexstr += "D"
        number -= 13
    elif number // 12 == 1:
        hexstr += "C"
        number -= 12
    elif number // 11 == 1:
        hexstr += "B"
        number -= 11
    elif number // 10 == 1:
        hexstr += "A"
        number -= 10
    elif number // 9 == 1:
        hexstr += "9"
        number -= 9
    elif number // 8 == 1:
        hexstr += "8"
        number -= 8
    elif number // 7 == 1:
        hexstr += "7"
        number -= 7
    elif number // 6 == 1:
        hexstr += "6"
        number -= 6
    elif number // 5 == 1:
        hexstr += "5"
        number -= 5
    elif number // 4 == 1:
        hexstr += "4"
        number -= 4
    elif number // 3 == 1:
        hexstr += "3"
        number -= 3
    elif number // 2 == 1:
        hexstr += "2"
        number -= 2
    elif number // 1 == 1:
        hexstr += "1"
        number -= 1
    elif number == 0:
        binstr += "0"
#    print(hexstr)
    return hexstr
def return_binary_recur(radice_recur, x=63, n=2, binstr=""):
    """ DOCSTRING: Inputs a number to convert to binary. First parameter is used only, others set to default. Recursive definition of conversion to binary from Dewey Decimal or base-10. Charles Thomas Wallace Truscott Watters, Byron Bay NSW 2481 """
#    print("radice: {} x: {} n: {} binstr: {}".format(radice_recur, x, 2, binstr))
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
    """ DOCSTRING: Inputs a number to convert to binary. First parameter is used only. Iterative definition of conversion to binary from Dewey Decimal or base-10. Charles Thomas Wallace Truscott Watters, Byron Bay NSW 2481 """

    n = 2
    binstr = str("")
    for x in range(63, 0, -1):
#        print("n: {} x: {} n ** x: {} radice: {}; radice // n ** x: {}".format(n, x, n ** x, radice, radice // (n ** x)))
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
#    print(binstr)
    return binstr
def return_binary(integer_n):
    """ DOCSTRING: Inputs a number to convert to binary. Charles Thomas Wallace Truscott Watters, Byron Bay NSW 2481 """
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

    return binary_string

def main():
    print("Charles Thomas Wallace Truscott Watters, student at MIT.\n\nMassachusetts Institute of Technology. QS globally #1 ranked college")
    print("Using recursion, 248124812481 in binary is: ")
    return_binary_recur(248124812481, 63, 2, "")
    print("Using iteration, 248124812481 in hexadecimal is: {}".format(return_hexadecimal_iter(248124812481)))
    print("Using iteration, 10041955 in binary is: {}".format(return_binary_iter(10041955)))
    print("15 and 255 in hex and binary are:\n\n{} and {}\n\nand {} and {}".format(return_hexadecimal_iter(15), return_binary_iter(15), return_hexadecimal_iter(255), return_binary_iter(255)))
if __name__ == "__main__":main()