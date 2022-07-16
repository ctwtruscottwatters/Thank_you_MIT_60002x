import os
import datetime

""" Authored by Charles Truscott Watters. Thank you Massachusetts Institute of Technology"""
""" Thank you John Guttag, Eric Grimson and Ana Bell and MIT staff and edX staff """
""" Silly string for Mathematics research
Sum: 20 (10 + 10) Difference: 0 ( 10 minus 10 )
Product: 100 (10 x 10) Reciprocal: 1 (10 / 10)
Power: 10000000000 (10 ^ 10)
20 (10 + 10) is a prime number?: False
0 (10 - 10) is a prime number?: None
10000000000 (10 to the power of 10) is a prime number?: False
Sum: 21 (10 + 11) Difference: -1 ( 10 minus 11 )
Product: 110 (10 x 11) Reciprocal: 0 (10 / 11)
Power: 100000000000 (10 ^ 11)
21 (10 + 11) is a prime number?: True
-1 (10 - 11) is a prime number?: None
100000000000 (10 to the power of 11) is a prime number?: False
Sum: 22 (10 + 12) Difference: -2 ( 10 minus 12 )
Product: 120 (10 x 12) Reciprocal: 0 (10 / 12)
Power: 1000000000000 (10 ^ 12)
22 (10 + 12) is a prime number?: False
-2 (10 - 12) is a prime number?: None
1000000000000 (10 to the power of 12) is a prime number?: False
Sum: 23 (10 + 13) Difference: -3 ( 10 minus 13 )
Product: 130 (10 x 13) Reciprocal: 0 (10 / 13)
Power: 10000000000000 (10 ^ 13)
23 (10 + 13) is a prime number?: True
-3 (10 - 13) is a prime number?: None
10000000000000 (10 to the power of 13) is a prime number?: False
Sum: 24 (10 + 14) Difference: -4 ( 10 minus 14 )
Product: 140 (10 x 14) Reciprocal: 0 (10 / 14)
Power: 100000000000000 (10 ^ 14)
24 (10 + 14) is a prime number?: False
-4 (10 - 14) is a prime number?: None
100000000000000 (10 to the power of 14) is a prime number?: False
Sum: 25 (10 + 15) Difference: -5 ( 10 minus 15 )
Product: 150 (10 x 15) Reciprocal: 0 (10 / 15)
Power: 1000000000000000 (10 ^ 15)
25 (10 + 15) is a prime number?: True
-5 (10 - 15) is a prime number?: None
1000000000000000 (10 to the power of 15) is a prime number?: False
Sum: 26 (10 + 16) Difference: -6 ( 10 minus 16 )
Product: 160 (10 x 16) Reciprocal: 0 (10 / 16)
Power: 10000000000000000 (10 ^ 16)
26 (10 + 16) is a prime number?: False
-6 (10 - 16) is a prime number?: None
10000000000000000 (10 to the power of 16) is a prime number?: False
Sum: 27 (10 + 17) Difference: -7 ( 10 minus 17 )
Product: 170 (10 x 17) Reciprocal: 0 (10 / 17)
Power: 100000000000000000 (10 ^ 17)
27 (10 + 17) is a prime number?: True
-7 (10 - 17) is a prime number?: None
100000000000000000 (10 to the power of 17) is a prime number?: False
Sum: 28 (10 + 18) Difference: -8 ( 10 minus 18 )
Product: 180 (10 x 18) Reciprocal: 0 (10 / 18)
Power: 1000000000000000000 (10 ^ 18)
28 (10 + 18) is a prime number?: False
-8 (10 - 18) is a prime number?: None
1000000000000000000 (10 to the power of 18) is a prime number?: False
Sum: 29 (10 + 19) Difference: -9 ( 10 minus 19 )
Product: 190 (10 x 19) Reciprocal: 0 (10 / 19)
Power: 10000000000000000000 (10 ^ 19)
29 (10 + 19) is a prime number?: True
-9 (10 - 19) is a prime number?: None
10000000000000000000 (10 to the power of 19) is a prime number?: False
Sum: 21 (11 + 10) Difference: 1 ( 11 minus 10 )
Product: 110 (11 x 10) Reciprocal: 1 (11 / 10)
Power: 25937424601 (11 ^ 10)
21 (11 + 10) is a prime number?: True
1 (11 - 10) is a prime number?: None
25937424601 (11 to the power of 10) is a prime number?: True
Sum: 22 (11 + 11) Difference: 0 ( 11 minus 11 )
Product: 121 (11 x 11) Reciprocal: 1 (11 / 11)
Power: 285311670611 (11 ^ 11)
22 (11 + 11) is a prime number?: False
0 (11 - 11) is a prime number?: None
285311670611 (11 to the power of 11) is a prime number?: True
Sum: 23 (11 + 12) Difference: -1 ( 11 minus 12 )
Product: 132 (11 x 12) Reciprocal: 0 (11 / 12)
Power: 3138428376721 (11 ^ 12)
23 (11 + 12) is a prime number?: True
-1 (11 - 12) is a prime number?: None
3138428376721 (11 to the power of 12) is a prime number?: True
Sum: 24 (11 + 13) Difference: -2 ( 11 minus 13 )
Product: 143 (11 x 13) Reciprocal: 0 (11 / 13)
Power: 34522712143931 (11 ^ 13)
24 (11 + 13) is a prime number?: False
-2 (11 - 13) is a prime number?: None
34522712143931 (11 to the power of 13) is a prime number?: True
Sum: 25 (11 + 14) Difference: -3 ( 11 minus 14 )
Product: 154 (11 x 14) Reciprocal: 0 (11 / 14)
Power: 379749833583241 (11 ^ 14)
25 (11 + 14) is a prime number?: True
-3 (11 - 14) is a prime number?: None
379749833583241 (11 to the power of 14) is a prime number?: True
Sum: 26 (11 + 15) Difference: -4 ( 11 minus 15 )
Product: 165 (11 x 15) Reciprocal: 0 (11 / 15)
Power: 4177248169415651 (11 ^ 15)
26 (11 + 15) is a prime number?: False
-4 (11 - 15) is a prime number?: None
4177248169415651 (11 to the power of 15) is a prime number?: True
Sum: 27 (11 + 16) Difference: -5 ( 11 minus 16 )
Product: 176 (11 x 16) Reciprocal: 0 (11 / 16)
Power: 45949729863572161 (11 ^ 16)
27 (11 + 16) is a prime number?: True
-5 (11 - 16) is a prime number?: None
45949729863572161 (11 to the power of 16) is a prime number?: True
Sum: 28 (11 + 17) Difference: -6 ( 11 minus 17 )
Product: 187 (11 x 17) Reciprocal: 0 (11 / 17)
Power: 505447028499293771 (11 ^ 17)
28 (11 + 17) is a prime number?: False
-6 (11 - 17) is a prime number?: None
505447028499293771 (11 to the power of 17) is a prime number?: True
Sum: 29 (11 + 18) Difference: -7 ( 11 minus 18 )
Product: 198 (11 x 18) Reciprocal: 0 (11 / 18)
Power: 5559917313492231481 (11 ^ 18)
29 (11 + 18) is a prime number?: True
-7 (11 - 18) is a prime number?: None
5559917313492231481 (11 to the power of 18) is a prime number?: True
Sum: 30 (11 + 19) Difference: -8 ( 11 minus 19 )
Product: 209 (11 x 19) Reciprocal: 0 (11 / 19)
Power: 61159090448414546291 (11 ^ 19)
30 (11 + 19) is a prime number?: False
-8 (11 - 19) is a prime number?: None
61159090448414546291 (11 to the power of 19) is a prime number?: True
Sum: 22 (12 + 10) Difference: 2 ( 12 minus 10 )
Product: 120 (12 x 10) Reciprocal: 1 (12 / 10)
Power: 61917364224 (12 ^ 10)
22 (12 + 10) is a prime number?: False
2 (12 - 10) is a prime number?: None
61917364224 (12 to the power of 10) is a prime number?: False
Sum: 23 (12 + 11) Difference: 1 ( 12 minus 11 )
Product: 132 (12 x 11) Reciprocal: 1 (12 / 11)
Power: 743008370688 (12 ^ 11)
23 (12 + 11) is a prime number?: True
1 (12 - 11) is a prime number?: None
743008370688 (12 to the power of 11) is a prime number?: False
Sum: 24 (12 + 12) Difference: 0 ( 12 minus 12 )
Product: 144 (12 x 12) Reciprocal: 1 (12 / 12)
Power: 8916100448256 (12 ^ 12)
24 (12 + 12) is a prime number?: False
0 (12 - 12) is a prime number?: None
8916100448256 (12 to the power of 12) is a prime number?: False
Sum: 25 (12 + 13) Difference: -1 ( 12 minus 13 )
Product: 156 (12 x 13) Reciprocal: 0 (12 / 13)
Power: 106993205379072 (12 ^ 13)
25 (12 + 13) is a prime number?: True
-1 (12 - 13) is a prime number?: None
106993205379072 (12 to the power of 13) is a prime number?: False
Sum: 26 (12 + 14) Difference: -2 ( 12 minus 14 )
Product: 168 (12 x 14) Reciprocal: 0 (12 / 14)
Power: 1283918464548864 (12 ^ 14)
26 (12 + 14) is a prime number?: False
-2 (12 - 14) is a prime number?: None
1283918464548864 (12 to the power of 14) is a prime number?: False
Sum: 27 (12 + 15) Difference: -3 ( 12 minus 15 )
Product: 180 (12 x 15) Reciprocal: 0 (12 / 15)
Power: 15407021574586368 (12 ^ 15)
27 (12 + 15) is a prime number?: True
-3 (12 - 15) is a prime number?: None
15407021574586368 (12 to the power of 15) is a prime number?: False
Sum: 28 (12 + 16) Difference: -4 ( 12 minus 16 )
Product: 192 (12 x 16) Reciprocal: 0 (12 / 16)
Power: 184884258895036416 (12 ^ 16)
28 (12 + 16) is a prime number?: False
-4 (12 - 16) is a prime number?: None
184884258895036416 (12 to the power of 16) is a prime number?: False
Sum: 29 (12 + 17) Difference: -5 ( 12 minus 17 )
Product: 204 (12 x 17) Reciprocal: 0 (12 / 17)
Power: 2218611106740436992 (12 ^ 17)
29 (12 + 17) is a prime number?: True
-5 (12 - 17) is a prime number?: None
2218611106740436992 (12 to the power of 17) is a prime number?: False
Sum: 30 (12 + 18) Difference: -6 ( 12 minus 18 )
Product: 216 (12 x 18) Reciprocal: 0 (12 / 18)
Power: 26623333280885243904 (12 ^ 18)
30 (12 + 18) is a prime number?: False
-6 (12 - 18) is a prime number?: None
26623333280885243904 (12 to the power of 18) is a prime number?: False
Sum: 31 (12 + 19) Difference: -7 ( 12 minus 19 )
Product: 228 (12 x 19) Reciprocal: 0 (12 / 19)
Power: 319479999370622926848 (12 ^ 19)
31 (12 + 19) is a prime number?: True
-7 (12 - 19) is a prime number?: None
319479999370622926848 (12 to the power of 19) is a prime number?: False
Sum: 23 (13 + 10) Difference: 3 ( 13 minus 10 )
Product: 130 (13 x 10) Reciprocal: 1 (13 / 10)
Power: 137858491849 (13 ^ 10)
23 (13 + 10) is a prime number?: True
3 (13 - 10) is a prime number?: True
137858491849 (13 to the power of 10) is a prime number?: True
Sum: 24 (13 + 11) Difference: 2 ( 13 minus 11 )
Product: 143 (13 x 11) Reciprocal: 1 (13 / 11)
Power: 1792160394037 (13 ^ 11)
24 (13 + 11) is a prime number?: False
2 (13 - 11) is a prime number?: None
1792160394037 (13 to the power of 11) is a prime number?: True
Sum: 25 (13 + 12) Difference: 1 ( 13 minus 12 )
Product: 156 (13 x 12) Reciprocal: 1 (13 / 12)
Power: 23298085122481 (13 ^ 12)
25 (13 + 12) is a prime number?: True
1 (13 - 12) is a prime number?: None
23298085122481 (13 to the power of 12) is a prime number?: True
Sum: 26 (13 + 13) Difference: 0 ( 13 minus 13 )
Product: 169 (13 x 13) Reciprocal: 1 (13 / 13)
Power: 302875106592253 (13 ^ 13)
26 (13 + 13) is a prime number?: False
0 (13 - 13) is a prime number?: None
302875106592253 (13 to the power of 13) is a prime number?: True
Sum: 27 (13 + 14) Difference: -1 ( 13 minus 14 )
Product: 182 (13 x 14) Reciprocal: 0 (13 / 14)
Power: 3937376385699289 (13 ^ 14)
27 (13 + 14) is a prime number?: True
-1 (13 - 14) is a prime number?: None
3937376385699289 (13 to the power of 14) is a prime number?: True
Sum: 28 (13 + 15) Difference: -2 ( 13 minus 15 )
Product: 195 (13 x 15) Reciprocal: 0 (13 / 15)
Power: 51185893014090757 (13 ^ 15)
28 (13 + 15) is a prime number?: False
-2 (13 - 15) is a prime number?: None
51185893014090757 (13 to the power of 15) is a prime number?: True
Sum: 29 (13 + 16) Difference: -3 ( 13 minus 16 )
Product: 208 (13 x 16) Reciprocal: 0 (13 / 16)
Power: 665416609183179841 (13 ^ 16)
29 (13 + 16) is a prime number?: True
-3 (13 - 16) is a prime number?: None
665416609183179841 (13 to the power of 16) is a prime number?: True
Sum: 30 (13 + 17) Difference: -4 ( 13 minus 17 )
Product: 221 (13 x 17) Reciprocal: 0 (13 / 17)
Power: 8650415919381337933 (13 ^ 17)
30 (13 + 17) is a prime number?: False
-4 (13 - 17) is a prime number?: None
8650415919381337933 (13 to the power of 17) is a prime number?: True
Sum: 31 (13 + 18) Difference: -5 ( 13 minus 18 )
Product: 234 (13 x 18) Reciprocal: 0 (13 / 18)
Power: 112455406951957393129 (13 ^ 18)
31 (13 + 18) is a prime number?: True
-5 (13 - 18) is a prime number?: None
112455406951957393129 (13 to the power of 18) is a prime number?: True
Sum: 32 (13 + 19) Difference: -6 ( 13 minus 19 )
Product: 247 (13 x 19) Reciprocal: 0 (13 / 19)
Power: 1461920290375446110677 (13 ^ 19)
32 (13 + 19) is a prime number?: False
-6 (13 - 19) is a prime number?: None
1461920290375446110677 (13 to the power of 19) is a prime number?: True
Sum: 24 (14 + 10) Difference: 4 ( 14 minus 10 )
Product: 140 (14 x 10) Reciprocal: 1 (14 / 10)
Power: 289254654976 (14 ^ 10)
24 (14 + 10) is a prime number?: False
4 (14 - 10) is a prime number?: False
289254654976 (14 to the power of 10) is a prime number?: False
Sum: 25 (14 + 11) Difference: 3 ( 14 minus 11 )
Product: 154 (14 x 11) Reciprocal: 1 (14 / 11)
Power: 4049565169664 (14 ^ 11)
25 (14 + 11) is a prime number?: True
3 (14 - 11) is a prime number?: True
4049565169664 (14 to the power of 11) is a prime number?: False
Sum: 26 (14 + 12) Difference: 2 ( 14 minus 12 )
Product: 168 (14 x 12) Reciprocal: 1 (14 / 12)
Power: 56693912375296 (14 ^ 12)
26 (14 + 12) is a prime number?: False
2 (14 - 12) is a prime number?: None
56693912375296 (14 to the power of 12) is a prime number?: False
Sum: 27 (14 + 13) Difference: 1 ( 14 minus 13 )
Product: 182 (14 x 13) Reciprocal: 1 (14 / 13)
Power: 793714773254144 (14 ^ 13)
27 (14 + 13) is a prime number?: True
1 (14 - 13) is a prime number?: None
793714773254144 (14 to the power of 13) is a prime number?: False
Sum: 28 (14 + 14) Difference: 0 ( 14 minus 14 )
Product: 196 (14 x 14) Reciprocal: 1 (14 / 14)
Power: 11112006825558016 (14 ^ 14)
28 (14 + 14) is a prime number?: False
0 (14 - 14) is a prime number?: None
11112006825558016 (14 to the power of 14) is a prime number?: False
Sum: 29 (14 + 15) Difference: -1 ( 14 minus 15 )
Product: 210 (14 x 15) Reciprocal: 0 (14 / 15)
Power: 155568095557812224 (14 ^ 15)
29 (14 + 15) is a prime number?: True
-1 (14 - 15) is a prime number?: None
155568095557812224 (14 to the power of 15) is a prime number?: False
Sum: 30 (14 + 16) Difference: -2 ( 14 minus 16 )
Product: 224 (14 x 16) Reciprocal: 0 (14 / 16)
Power: 2177953337809371136 (14 ^ 16)
30 (14 + 16) is a prime number?: False
-2 (14 - 16) is a prime number?: None
2177953337809371136 (14 to the power of 16) is a prime number?: False
Sum: 31 (14 + 17) Difference: -3 ( 14 minus 17 )
Product: 238 (14 x 17) Reciprocal: 0 (14 / 17)
Power: 30491346729331195904 (14 ^ 17)
31 (14 + 17) is a prime number?: True
-3 (14 - 17) is a prime number?: None
30491346729331195904 (14 to the power of 17) is a prime number?: False
Sum: 32 (14 + 18) Difference: -4 ( 14 minus 18 )
Product: 252 (14 x 18) Reciprocal: 0 (14 / 18)
Power: 426878854210636742656 (14 ^ 18)
32 (14 + 18) is a prime number?: False
-4 (14 - 18) is a prime number?: None
426878854210636742656 (14 to the power of 18) is a prime number?: False
Sum: 33 (14 + 19) Difference: -5 ( 14 minus 19 )
Product: 266 (14 x 19) Reciprocal: 0 (14 / 19)
Power: 5976303958948914397184 (14 ^ 19)
33 (14 + 19) is a prime number?: True
-5 (14 - 19) is a prime number?: None
5976303958948914397184 (14 to the power of 19) is a prime number?: False
Sum: 25 (15 + 10) Difference: 5 ( 15 minus 10 )
Product: 150 (15 x 10) Reciprocal: 1 (15 / 10)
Power: 576650390625 (15 ^ 10)
25 (15 + 10) is a prime number?: True
5 (15 - 10) is a prime number?: True
576650390625 (15 to the power of 10) is a prime number?: True
Sum: 26 (15 + 11) Difference: 4 ( 15 minus 11 )
Product: 165 (15 x 11) Reciprocal: 1 (15 / 11)
Power: 8649755859375 (15 ^ 11)
26 (15 + 11) is a prime number?: False
4 (15 - 11) is a prime number?: False
8649755859375 (15 to the power of 11) is a prime number?: True
Sum: 27 (15 + 12) Difference: 3 ( 15 minus 12 )
Product: 180 (15 x 12) Reciprocal: 1 (15 / 12)
Power: 129746337890625 (15 ^ 12)
27 (15 + 12) is a prime number?: True
3 (15 - 12) is a prime number?: True
129746337890625 (15 to the power of 12) is a prime number?: True
Sum: 28 (15 + 13) Difference: 2 ( 15 minus 13 )
Product: 195 (15 x 13) Reciprocal: 1 (15 / 13)
Power: 1946195068359375 (15 ^ 13)
28 (15 + 13) is a prime number?: False
2 (15 - 13) is a prime number?: None
1946195068359375 (15 to the power of 13) is a prime number?: True
Sum: 29 (15 + 14) Difference: 1 ( 15 minus 14 )
Product: 210 (15 x 14) Reciprocal: 1 (15 / 14)
Power: 29192926025390625 (15 ^ 14)
29 (15 + 14) is a prime number?: True
1 (15 - 14) is a prime number?: None
29192926025390625 (15 to the power of 14) is a prime number?: True
Sum: 30 (15 + 15) Difference: 0 ( 15 minus 15 )
Product: 225 (15 x 15) Reciprocal: 1 (15 / 15)
Power: 437893890380859375 (15 ^ 15)
30 (15 + 15) is a prime number?: False
0 (15 - 15) is a prime number?: None
437893890380859375 (15 to the power of 15) is a prime number?: True
Sum: 31 (15 + 16) Difference: -1 ( 15 minus 16 )
Product: 240 (15 x 16) Reciprocal: 0 (15 / 16)
Power: 6568408355712890625 (15 ^ 16)
31 (15 + 16) is a prime number?: True
-1 (15 - 16) is a prime number?: None
6568408355712890625 (15 to the power of 16) is a prime number?: True
Sum: 32 (15 + 17) Difference: -2 ( 15 minus 17 )
Product: 255 (15 x 17) Reciprocal: 0 (15 / 17)
Power: 98526125335693359375 (15 ^ 17)
32 (15 + 17) is a prime number?: False
-2 (15 - 17) is a prime number?: None
98526125335693359375 (15 to the power of 17) is a prime number?: True
Sum: 33 (15 + 18) Difference: -3 ( 15 minus 18 )
Product: 270 (15 x 18) Reciprocal: 0 (15 / 18)
Power: 1477891880035400390625 (15 ^ 18)
33 (15 + 18) is a prime number?: True
-3 (15 - 18) is a prime number?: None
1477891880035400390625 (15 to the power of 18) is a prime number?: True
Sum: 34 (15 + 19) Difference: -4 ( 15 minus 19 )
Product: 285 (15 x 19) Reciprocal: 0 (15 / 19)
Power: 22168378200531005859375 (15 ^ 19)
34 (15 + 19) is a prime number?: False
-4 (15 - 19) is a prime number?: None
22168378200531005859375 (15 to the power of 19) is a prime number?: True
Sum: 26 (16 + 10) Difference: 6 ( 16 minus 10 )
Product: 160 (16 x 10) Reciprocal: 1 (16 / 10)
Power: 1099511627776 (16 ^ 10)
26 (16 + 10) is a prime number?: False
6 (16 - 10) is a prime number?: False
1099511627776 (16 to the power of 10) is a prime number?: False
Sum: 27 (16 + 11) Difference: 5 ( 16 minus 11 )
Product: 176 (16 x 11) Reciprocal: 1 (16 / 11)
Power: 17592186044416 (16 ^ 11)
27 (16 + 11) is a prime number?: True
5 (16 - 11) is a prime number?: True
17592186044416 (16 to the power of 11) is a prime number?: False
Sum: 28 (16 + 12) Difference: 4 ( 16 minus 12 )
Product: 192 (16 x 12) Reciprocal: 1 (16 / 12)
Power: 281474976710656 (16 ^ 12)
28 (16 + 12) is a prime number?: False
4 (16 - 12) is a prime number?: False
281474976710656 (16 to the power of 12) is a prime number?: False
Sum: 29 (16 + 13) Difference: 3 ( 16 minus 13 )
Product: 208 (16 x 13) Reciprocal: 1 (16 / 13)
Power: 4503599627370496 (16 ^ 13)
29 (16 + 13) is a prime number?: True
3 (16 - 13) is a prime number?: True
4503599627370496 (16 to the power of 13) is a prime number?: False
Sum: 30 (16 + 14) Difference: 2 ( 16 minus 14 )
Product: 224 (16 x 14) Reciprocal: 1 (16 / 14)
Power: 72057594037927936 (16 ^ 14)
30 (16 + 14) is a prime number?: False
2 (16 - 14) is a prime number?: None
72057594037927936 (16 to the power of 14) is a prime number?: False
Sum: 31 (16 + 15) Difference: 1 ( 16 minus 15 )
Product: 240 (16 x 15) Reciprocal: 1 (16 / 15)
Power: 1152921504606846976 (16 ^ 15)
31 (16 + 15) is a prime number?: True
1 (16 - 15) is a prime number?: None
1152921504606846976 (16 to the power of 15) is a prime number?: False
Sum: 32 (16 + 16) Difference: 0 ( 16 minus 16 )
Product: 256 (16 x 16) Reciprocal: 1 (16 / 16)
Power: 18446744073709551616 (16 ^ 16)
32 (16 + 16) is a prime number?: False
0 (16 - 16) is a prime number?: None
18446744073709551616 (16 to the power of 16) is a prime number?: False
Sum: 33 (16 + 17) Difference: -1 ( 16 minus 17 )
Product: 272 (16 x 17) Reciprocal: 0 (16 / 17)
Power: 295147905179352825856 (16 ^ 17)
33 (16 + 17) is a prime number?: True
-1 (16 - 17) is a prime number?: None
295147905179352825856 (16 to the power of 17) is a prime number?: False
Sum: 34 (16 + 18) Difference: -2 ( 16 minus 18 )
Product: 288 (16 x 18) Reciprocal: 0 (16 / 18)
Power: 4722366482869645213696 (16 ^ 18)
34 (16 + 18) is a prime number?: False
-2 (16 - 18) is a prime number?: None
4722366482869645213696 (16 to the power of 18) is a prime number?: False
Sum: 35 (16 + 19) Difference: -3 ( 16 minus 19 )
Product: 304 (16 x 19) Reciprocal: 0 (16 / 19)
Power: 75557863725914323419136 (16 ^ 19)
35 (16 + 19) is a prime number?: True
-3 (16 - 19) is a prime number?: None
75557863725914323419136 (16 to the power of 19) is a prime number?: False
Sum: 27 (17 + 10) Difference: 7 ( 17 minus 10 )
Product: 170 (17 x 10) Reciprocal: 1 (17 / 10)
Power: 2015993900449 (17 ^ 10)
27 (17 + 10) is a prime number?: True
7 (17 - 10) is a prime number?: True
2015993900449 (17 to the power of 10) is a prime number?: True
Sum: 28 (17 + 11) Difference: 6 ( 17 minus 11 )
Product: 187 (17 x 11) Reciprocal: 1 (17 / 11)
Power: 34271896307633 (17 ^ 11)
28 (17 + 11) is a prime number?: False
6 (17 - 11) is a prime number?: False
34271896307633 (17 to the power of 11) is a prime number?: True
Sum: 29 (17 + 12) Difference: 5 ( 17 minus 12 )
Product: 204 (17 x 12) Reciprocal: 1 (17 / 12)
Power: 582622237229761 (17 ^ 12)
29 (17 + 12) is a prime number?: True
5 (17 - 12) is a prime number?: True
582622237229761 (17 to the power of 12) is a prime number?: True
Sum: 30 (17 + 13) Difference: 4 ( 17 minus 13 )
Product: 221 (17 x 13) Reciprocal: 1 (17 / 13)
Power: 9904578032905937 (17 ^ 13)
30 (17 + 13) is a prime number?: False
4 (17 - 13) is a prime number?: False
9904578032905937 (17 to the power of 13) is a prime number?: True
Sum: 31 (17 + 14) Difference: 3 ( 17 minus 14 )
Product: 238 (17 x 14) Reciprocal: 1 (17 / 14)
Power: 168377826559400929 (17 ^ 14)
31 (17 + 14) is a prime number?: True
3 (17 - 14) is a prime number?: True
168377826559400929 (17 to the power of 14) is a prime number?: True
Sum: 32 (17 + 15) Difference: 2 ( 17 minus 15 )
Product: 255 (17 x 15) Reciprocal: 1 (17 / 15)
Power: 2862423051509815793 (17 ^ 15)
32 (17 + 15) is a prime number?: False
2 (17 - 15) is a prime number?: None
2862423051509815793 (17 to the power of 15) is a prime number?: True
Sum: 33 (17 + 16) Difference: 1 ( 17 minus 16 )
Product: 272 (17 x 16) Reciprocal: 1 (17 / 16)
Power: 48661191875666868481 (17 ^ 16)
33 (17 + 16) is a prime number?: True
1 (17 - 16) is a prime number?: None
48661191875666868481 (17 to the power of 16) is a prime number?: True
Sum: 34 (17 + 17) Difference: 0 ( 17 minus 17 )
Product: 289 (17 x 17) Reciprocal: 1 (17 / 17)
Power: 827240261886336764177 (17 ^ 17)
34 (17 + 17) is a prime number?: False
0 (17 - 17) is a prime number?: None
827240261886336764177 (17 to the power of 17) is a prime number?: True
Sum: 35 (17 + 18) Difference: -1 ( 17 minus 18 )
Product: 306 (17 x 18) Reciprocal: 0 (17 / 18)
Power: 14063084452067724991009 (17 ^ 18)
35 (17 + 18) is a prime number?: True
-1 (17 - 18) is a prime number?: None
14063084452067724991009 (17 to the power of 18) is a prime number?: True
Sum: 36 (17 + 19) Difference: -2 ( 17 minus 19 )
Product: 323 (17 x 19) Reciprocal: 0 (17 / 19)
Power: 239072435685151324847153 (17 ^ 19)
36 (17 + 19) is a prime number?: False
-2 (17 - 19) is a prime number?: None
239072435685151324847153 (17 to the power of 19) is a prime number?: True
Sum: 28 (18 + 10) Difference: 8 ( 18 minus 10 )
Product: 180 (18 x 10) Reciprocal: 1 (18 / 10)
Power: 3570467226624 (18 ^ 10)
28 (18 + 10) is a prime number?: False
8 (18 - 10) is a prime number?: False
3570467226624 (18 to the power of 10) is a prime number?: False
Sum: 29 (18 + 11) Difference: 7 ( 18 minus 11 )
Product: 198 (18 x 11) Reciprocal: 1 (18 / 11)
Power: 64268410079232 (18 ^ 11)
29 (18 + 11) is a prime number?: True
7 (18 - 11) is a prime number?: True
64268410079232 (18 to the power of 11) is a prime number?: False
Sum: 30 (18 + 12) Difference: 6 ( 18 minus 12 )
Product: 216 (18 x 12) Reciprocal: 1 (18 / 12)
Power: 1156831381426176 (18 ^ 12)
30 (18 + 12) is a prime number?: False
6 (18 - 12) is a prime number?: False
1156831381426176 (18 to the power of 12) is a prime number?: False
Sum: 31 (18 + 13) Difference: 5 ( 18 minus 13 )
Product: 234 (18 x 13) Reciprocal: 1 (18 / 13)
Power: 20822964865671168 (18 ^ 13)
31 (18 + 13) is a prime number?: True
5 (18 - 13) is a prime number?: True
20822964865671168 (18 to the power of 13) is a prime number?: False
Sum: 32 (18 + 14) Difference: 4 ( 18 minus 14 )
Product: 252 (18 x 14) Reciprocal: 1 (18 / 14)
Power: 374813367582081024 (18 ^ 14)
32 (18 + 14) is a prime number?: False
4 (18 - 14) is a prime number?: False
374813367582081024 (18 to the power of 14) is a prime number?: False
Sum: 33 (18 + 15) Difference: 3 ( 18 minus 15 )
Product: 270 (18 x 15) Reciprocal: 1 (18 / 15)
Power: 6746640616477458432 (18 ^ 15)
33 (18 + 15) is a prime number?: True
3 (18 - 15) is a prime number?: True
6746640616477458432 (18 to the power of 15) is a prime number?: False
Sum: 34 (18 + 16) Difference: 2 ( 18 minus 16 )
Product: 288 (18 x 16) Reciprocal: 1 (18 / 16)
Power: 121439531096594251776 (18 ^ 16)
34 (18 + 16) is a prime number?: False
2 (18 - 16) is a prime number?: None
121439531096594251776 (18 to the power of 16) is a prime number?: False
Sum: 35 (18 + 17) Difference: 1 ( 18 minus 17 )
Product: 306 (18 x 17) Reciprocal: 1 (18 / 17)
Power: 2185911559738696531968 (18 ^ 17)
35 (18 + 17) is a prime number?: True
1 (18 - 17) is a prime number?: None
2185911559738696531968 (18 to the power of 17) is a prime number?: False
Sum: 36 (18 + 18) Difference: 0 ( 18 minus 18 )
Product: 324 (18 x 18) Reciprocal: 1 (18 / 18)
Power: 39346408075296537575424 (18 ^ 18)
36 (18 + 18) is a prime number?: False
0 (18 - 18) is a prime number?: None
39346408075296537575424 (18 to the power of 18) is a prime number?: False
Sum: 37 (18 + 19) Difference: -1 ( 18 minus 19 )
Product: 342 (18 x 19) Reciprocal: 0 (18 / 19)
Power: 708235345355337676357632 (18 ^ 19)
37 (18 + 19) is a prime number?: True
-1 (18 - 19) is a prime number?: None
708235345355337676357632 (18 to the power of 19) is a prime number?: False
Sum: 29 (19 + 10) Difference: 9 ( 19 minus 10 )
Product: 190 (19 x 10) Reciprocal: 1 (19 / 10)
Power: 6131066257801 (19 ^ 10)
29 (19 + 10) is a prime number?: True
9 (19 - 10) is a prime number?: True
6131066257801 (19 to the power of 10) is a prime number?: True
Sum: 30 (19 + 11) Difference: 8 ( 19 minus 11 )
Product: 209 (19 x 11) Reciprocal: 1 (19 / 11)
Power: 116490258898219 (19 ^ 11)
30 (19 + 11) is a prime number?: False
8 (19 - 11) is a prime number?: False
116490258898219 (19 to the power of 11) is a prime number?: True
Sum: 31 (19 + 12) Difference: 7 ( 19 minus 12 )
Product: 228 (19 x 12) Reciprocal: 1 (19 / 12)
Power: 2213314919066161 (19 ^ 12)
31 (19 + 12) is a prime number?: True
7 (19 - 12) is a prime number?: True
2213314919066161 (19 to the power of 12) is a prime number?: True
Sum: 32 (19 + 13) Difference: 6 ( 19 minus 13 )
Product: 247 (19 x 13) Reciprocal: 1 (19 / 13)
Power: 42052983462257059 (19 ^ 13)
32 (19 + 13) is a prime number?: False
6 (19 - 13) is a prime number?: False
42052983462257059 (19 to the power of 13) is a prime number?: True
Sum: 33 (19 + 14) Difference: 5 ( 19 minus 14 )
Product: 266 (19 x 14) Reciprocal: 1 (19 / 14)
Power: 799006685782884121 (19 ^ 14)
33 (19 + 14) is a prime number?: True
5 (19 - 14) is a prime number?: True
799006685782884121 (19 to the power of 14) is a prime number?: True
Sum: 34 (19 + 15) Difference: 4 ( 19 minus 15 )
Product: 285 (19 x 15) Reciprocal: 1 (19 / 15)
Power: 15181127029874798299 (19 ^ 15)
34 (19 + 15) is a prime number?: False
4 (19 - 15) is a prime number?: False
15181127029874798299 (19 to the power of 15) is a prime number?: True
Sum: 35 (19 + 16) Difference: 3 ( 19 minus 16 )
Product: 304 (19 x 16) Reciprocal: 1 (19 / 16)
Power: 288441413567621167681 (19 ^ 16)
35 (19 + 16) is a prime number?: True
3 (19 - 16) is a prime number?: True
288441413567621167681 (19 to the power of 16) is a prime number?: True
Sum: 36 (19 + 17) Difference: 2 ( 19 minus 17 )
Product: 323 (19 x 17) Reciprocal: 1 (19 / 17)
Power: 5480386857784802185939 (19 ^ 17)
36 (19 + 17) is a prime number?: False
2 (19 - 17) is a prime number?: None
5480386857784802185939 (19 to the power of 17) is a prime number?: True
Sum: 37 (19 + 18) Difference: 1 ( 19 minus 18 )
Product: 342 (19 x 18) Reciprocal: 1 (19 / 18)
Power: 104127350297911241532841 (19 ^ 18)
37 (19 + 18) is a prime number?: True
1 (19 - 18) is a prime number?: None
104127350297911241532841 (19 to the power of 18) is a prime number?: True
Sum: 38 (19 + 19) Difference: 0 ( 19 minus 19 )
Product: 361 (19 x 19) Reciprocal: 1 (19 / 19)
Power: 1978419655660313589123979 (19 ^ 19)
38 (19 + 19) is a prime number?: False
0 (19 - 19) is a prime number?: None
1978419655660313589123979 (19 to the power of 19) is a prime number?: True
""" 

class ArithmeticOperations(object):
    def __init__(self, a=0, b=0, c=0, d=0, e=0, f=0, g=0, h=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
    def add(self):
        count_one = 0
        count_two = 0
        count_three = 0
        count_four = self.a
        count_five = self.b
        while count_four is not 0:
            count_one += 1
            count_four -= 1
            #print(count_one, a)
        while count_five is not 0:
            count_two += 1
            count_five -= 1
            #print(count_two, b)
        #print(a, b, count_one, count_two)
        for x in range(0, count_one + count_two, 1):
            #print(count_three)
            count_three += 1

        return count_three
    def subtract(self):
        subtrahend = self.a - self.b
        return subtrahend

    def multiply(self):
        multiplicand = self.a * self.b
        return multiplicand

    def divide(self):
        no_remainder = self.a // self.b
        return no_remainder
    def exponentiate(self):
        base = self.a
        exponent = self.b
        exponent_copy = self.b
        while exponent_copy is not 1:
            #print(base, exponent)
            base *= self.a
            exponent_copy -= 1
        power = base
        return power

def is_prime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
        else:
            return True

def main():
    new = ArithmeticOperations(5, 3)
    print(new.add())
    print(new.exponentiate())
    count = 0
    p = []
    q = []
    r = []
    s = []
    for x in range (10, 20, 1):
        for y in range(10, 20, 1):
            count += 1
            temp = ArithmeticOperations(x, y)
            p += [["Sum", x, y, temp.add()]]
            p += [["Reciprocal", x, y, temp.divide()]]
            q += [["Product", x, y, temp.multiply()]]
            q += [["Exponent", x, y, temp.exponentiate()]]
            r += [["Difference", x, y, temp.subtract()]]
            r += [["Sum Squared", x, y, temp.add() ** 2]]
            s += [["Exponent halved", x, y, temp.exponentiate() // 2]]
            print("Sum: {} ({} + {}) Difference: {} ( {} minus {} )".format(str(temp.add()), str(x), str(y), str(temp.subtract()), str(x), str(y)))
            print("Product: {} ({} x {}) Reciprocal: {} ({} / {})".format(str(temp.multiply()), str(x), str(y), temp.divide(), str(x), str(y)))
            print("Power: {} ({} ^ {})".format(str(temp.exponentiate()), str(x), str(y)))
            print("{} ({} + {}) is a prime number?: {}".format(str(temp.add()), str(x), str(y), is_prime(temp.add())))
            print("{} ({} - {}) is a prime number?: {}".format(str(temp.subtract()), str(x), str(y), is_prime(temp.subtract())))
            print("{} ({} to the power of {}) is a prime number?: {}".format(str(temp.exponentiate()), str(x), str(y), is_prime(temp.exponentiate())))

            # What about writing Fermat's Last Theorem
            temp = 0
    #print(p, q, r, s)
    reference = []
    for a in p:
        for b in q:
            for c in r:
                for d in s:
                    print(a, b, c, d)
                    if type(a) == list and type(b):
                        if a[3] == b[3] and a[3] > 5 and a[0] is not "Sum" and b[0] is not "Difference":
                            print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(a[3], b[3], a[0], a[1], a[2], b[0], b[1], b[2]))
                    if type(c) == list and type(a) == list:
                        if a[3] == c[3] and a[3] > 5 and a[0] is not "Sum" and c[0] is not "Difference":
                            print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(a[3], c[3], a[0], a[1], a[2], c[0], c[1], c[2]))
                    if type(a) == list and type(d) == list:
                        if a[3] == d[3] and a[3] > 5 and a[0] is not "Sum" and d[0] is not "Difference":
                            print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(a[3], d[3], a[0], a[1], a[2], d[0], d[1], d[2]))
                    if type(b) == list and type(c) == list:
                        if b[3] == c[3] and b[3] > 5 and b[0] is not "Sum" and c[0] is not "Difference":
                            print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(b[3], c[3], b[0], b[1], b[2], c[0], c[1], c[2]))
                    if type(b) == list and type(d) == list:
                        if b[3] == d[3] and b[3] > 5 and b[0] is not "Sum" and c[0] is not "Difference":
                            print("{} equals {} which is the {} of {} and {} and the {} of {} and {}".format(b[3], d[3], b[0], b[1], b[2], d[0], d[1], d[2]))

    # Mathematical Proofs in Python hopefully
    print("Charles Truscott Watters")
if __name__ == "__main__": main()