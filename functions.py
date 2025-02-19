from bracket_check import *
import re


def sqrt_p(listy: list):
    # print('found sqrt_p...')
    for i in range(len(listy)):
        if listy[i] == "/p/":
            pair = last_pair(listy[:i])
            first_args = listy[: i - len(pair)]
            second_args = listy[i + 1 :]
            pair_two = next_pair(second_args)
            # print(first_args, " and ", second_args)

            # new_listy = first_args + ["sqrt", "("] + pair + ["**", "2", "+"] + pair_two + ["**", "2", ")"] + second_args[len(pair_two):]
            new_listy = first_args
            new_listy.append("math.sqrt")
            new_listy.append("(")
            new_listy += pair
            new_listy.append("**")
            new_listy.append("2")
            new_listy.append("+")
            new_listy += pair_two
            new_listy.append("**")
            new_listy.append("2")
            new_listy.append(")")
            new_listy += second_args[len(pair_two) :]
            # print("new_listy: ", new_listy)
            return new_listy

def sqrt(listy: list):
    # print('found sqrt_p...')
    new_listy = []
    for i in range(len(listy)):
        if listy[i] == "sqrt":
            if listy[i-1] == ')':
                pair = last_pair(listy[:i])
                # print("pair:", pair)
                first_args = listy[: i - len(pair)+1]
                second_args = listy[i + 1 :]
                
                # print(first_args, " and ", second_args)

                # new_listy = first_args + ["sqrt", "("] + pair + ["**", "2", "+"] + pair_two + ["**", "2", ")"] + second_args[len(pair_two):]
                new_listy = first_args
                new_listy.append("math.sqrt")
                new_listy.append("(")
                new_listy += pair
                # new_listy += pair_two
                new_listy.append(")")
                new_listy += second_args[len(first_args)+len(pair):]
                # print("second_args[len(first_args)+len(pair):]: ", second_args[len(first_args)+len(pair):])
                # print("new_listy: ", new_listy)
                while not is_balanced(new_listy):  # Проверка на сбалансированность скобок
                    new_listy.append(")")
                return new_listy
            else:
                left_part = listy[:i-1]     
                main_part = listy[i-1]
                right_part = listy[i+1:]
                new_listy += left_part
                new_listy.append("math.sqrt")
                new_listy.append("(")
                new_listy += main_part
                
                new_listy.append(")")
                new_listy += right_part
                return new_listy
                           
def lg(listy: list):
    # print('found log10...')
    # print("WTF IS HERE???")
    for i in range(len(listy)):
        if listy[i] == "lg":
            pair = last_pair(listy[:i])
            # print("pair:", pair)
            first_args = listy[: i - len(pair)]
            second_args = listy[i + 1 :]
            # print(first_args, " and2 ", second_args)

            new_listy = first_args
            new_listy.append("math.log10")
            new_listy.append("(")
            new_listy += pair
            new_listy.append(")")
            new_listy += second_args
            return new_listy


def trigonometr(listy: list):
    for i in range(len(listy)):
        if listy[i] == "sin" or listy[i] == "cos" or listy[i] == "tan" or listy[i] == "cot":
            # print(f'found {listy[i]}...')
            pair = last_pair(listy[:i])
            # print("pair:", pair)
            first_args = listy[: i - len(pair)]
            second_args = listy[i + 1 :]
            # print(first_args, " and2 ", second_args)
            # print(listy[i])
            new_listy = first_args
            if listy[i] == "sin":
                new_listy.append("math.sin")
            elif listy[i] == "cos":
                new_listy.append("math.cos")
            elif listy[i] == "tan":
                new_listy.append("math.tan")
            new_listy.append("(")
            new_listy += pair
            new_listy.append(")")
            new_listy += second_args
            return new_listy


def ln(listy: list):
    for i in range(len(listy)):
        if listy[i] == "ln":
            pair = last_pair(listy[:i])
            # print("pair:", pair)
            first_args = listy[: i - len(pair)]
            second_args = listy[i + 1 :]
            # print(first_args, " and2 ", second_args)

            new_listy = first_args
            new_listy.append("math.log")
            new_listy.append("(")
            new_listy += pair
            new_listy.append(")")
            new_listy += second_args
            # print(new_listy)
            return new_listy


def degree_y(listy: list):
    for i in range(len(listy)):
        if listy[i] == "y^x":
            pair = last_pair(listy[:i])
            # print("pair:", pair)
            first_args = listy[: i - len(pair)]
            second_args = listy[i + 1 :]
            pair_two = next_pair(second_args)

            # print(first_args, " and2 ", second_args)

            new_listy = first_args
            new_listy.append("(")
            new_listy += pair
            new_listy.append("**")
            new_listy += pair_two
            new_listy.append(")")
            # print('pair_two len: ', len(pair_two))
            new_listy += second_args[len(pair_two) :]
            return new_listy


def reverse_x(listy: list):
    print("listy:", listy)
    addition = []
    new_listy = []
    for i in range(len(listy)):
        if listy[i] == "1/":
            pair = last_pair(listy[:i])
            print("pair:", pair)
            first_args = listy[: i - len(pair)]
            previous_val = [first_args[len(first_args) - 1]]
            print(
                "previous_val:",
                previous_val,
                re.match(r"^-?\d+(\.\d+)?$", previous_val[0]),
            )
            if previous_val[0] not in {"-", "+", "*", "/", ")", "("} and not re.match(
                r"^-?\d+(\.\d+)?$", previous_val[0]
            ):
                addition = previous_val
                print("addition:", addition)
            second_args = listy[i + 1 :]

            # print(first_args, " and2 ", second_args)

            new_listy = first_args
            if addition:
                new_listy.pop()
            new_listy.append("(")
            new_listy.append("1")
            new_listy.append("/")
            if addition:
                new_listy += addition
            new_listy += pair
            new_listy.append(")")
            new_listy += second_args

    return new_listy
