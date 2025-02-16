from parser import *


def test_val(input_val, real_val, file):

    print(input_val)
    eps = input_val / real_val
    print("EPS:", eps)
    if 0.80 < eps < 1.2:
        file.write(f"SUCCESSED EVALUATION -- {input_val} comp with {real_val}\n")
    else:
        file.write(f"FAILED EVALUATION -- {input_val} comp with {real_val}\n")


# TEST

testf = open("tests.txt", "w")

# нужно 3 + 4 * ( ( 7 /p/ 9 * 25 ) lg + 6 = преобразовать в 3  + 4 * lg ( sqrt ( 7 ^ 2 + 9 ^ 2) * 25 + 6) =
input_val = [
    "3",
    "+",
    "4",
    "*",
    "(",
    "(",
    "7",
    "/p/",
    "9",
    "*",
    "25",
    ")",
    "lg",
    "+",
    "6",
]
real_val = 3.681964673 * 10**1
test_val(rez(input_val), real_val, testf)


# 3 + 2 * 7 y^x 2 преобразовать в 3 + 2 * 7 ** 2
input_val = ["3", "+", "2", "*", "7", "y^x", "2"]
real_val = 1.01 * 10**2
test_val(rez(input_val), real_val, testf)

# 4 * 5 / 7 + 29 / 3 * 11 ) * ( 19 / ( 2 + 4 ) + ( 13 + Pi ) / 4 = преобразовать в ( 4 * 5 / 7 + 29 / 3 * 11 ) * ( 19 / ( 2 + 4 ) + ( 13 + 3,1415926 ) / 4 )

input_val = [
    "4",
    "*",
    "5",
    "/",
    "7",
    "+",
    "29",
    "/",
    "(",
    "3",
    "*",
    "11",
    ")",
    ")",
    "*",
    "(",
    "19",
    "/",
    "(",
    "2",
    "+",
    "4",
    ")",
    "+",
    "(",
    "13",
    "+",
    "3.1415926",
    ")",
    "/",
    "4",
]
real_val = 2.690641536 * 10**1
test_val(rez(input_val), real_val, testf)

input_val = parse_expression(
    "4 * 5 / 7 + 29 / ( 3 * 11 ) ) * ( 19 / ( 2 + 4 ) + ( 13 + 3.1415926 ) / 4"
)
real_val = 2.690641536 * 10**1
test_val(rez(input_val), real_val, testf)


# ln
input_val = parse_expression("3 + 4 * ( ( 7 /p/ 9 * 25 ) ln + 6")
real_val = 49.61057
test_val(rez(input_val), real_val, testf)

# sin
input_val = parse_expression("6 sin + ( 6 + 8 ) sin")
real_val = 0.711192
test_val(rez(input_val), real_val, testf)

# cos
input_val = parse_expression("6 cos + ( 6 + 8 ) cos")
real_val = 1.09691
test_val(rez(input_val), real_val, testf)

# tan
input_val = parse_expression("6 tan + ( 6 + 8 ) tan")
real_val = 6.9536
test_val(rez(input_val), real_val, testf)
# 1/
input_val = parse_expression(
    "4 * 5 / 7 + 29 / ( 3 * 11 ) ) * ( 19 / ( 2 + 4 ) + ( 13 + 3.1415926 ) / 4 1/"
)
real_val = 19.354
test_val(rez(input_val), real_val, testf)

input_val = parse_expression("6 tan + ( 6 + 8 ) tan 1/")
real_val = -0.152972
test_val(rez(input_val), real_val, testf)

input_val = parse_expression("3 + 9 sqrt")
real_val = 6
test_val(rez(input_val), real_val, testf)

input_val = parse_expression(" 3 + 6 ) sqrt")
real_val = 3
test_val(rez(input_val), real_val, testf)

input_val = parse_expression("( 3 + 6 ) sqrt")
real_val = 3
test_val(rez(input_val), real_val, testf)

input_val = parse_expression("4 + ( 3 + 6 ) sqrt")
real_val = 7
test_val(rez(input_val), real_val, testf)


testf.close()
