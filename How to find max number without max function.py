numbers = [52,
80,
56,
50,
56,
55,
67,
40,
52,
43,
65,
47,
46,
58,
70,
72,
62,
65,
67,
73,
52,
69,
57,
43,
65,
82,
40,
50,
45,
57,
70,
39,
65,
60,
38,
69,
52,
74,
95,
58,
60,
61,
57,
60,
74,
55,
65,
55,
62,
58,
55,
55,
80,
65,
53,
53,
70,
60,
51,
58,
75,
40,
55,
60,
65,
53,
40,
88,
55,
52,
72,
61,
94,
86,
64,
43,
49,
54,
38,
62,
60,
58,
58,
60]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

max = 0
for number in numbers:
    if number >= 94 and number <= 101:
        max += 1
print(max)
print(len(numbers))