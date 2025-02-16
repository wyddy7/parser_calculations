import math
from bracket_check import *
from functions import *


def transform_list(list):
    if not list:
        return []
    new_list = []
    operations = {
        "/p/": sqrt_p,
        "lg": lg,
        "ln": ln,
        "y^x": degree_y,
        "sin": trigonometr,
        "cos": trigonometr,
        "tan": trigonometr,
        "1/": reverse_x,
    }

    for item in list:
        if item in operations:
            func = operations[item]
            new_list = func(new_list if new_list else list)

            if new_list is None:
                raise ValueError("Одна из функций вернула None. Проверьте реализацию.")
            if item == list[len(list) - 1] and not new_list:
                new_list = list

    return new_list if new_list else list


def rez(input_val):
    print("--Getting new value...")
    if not is_balanced(input_val):  # Проверка на сбалансированность скобок
        input_val.insert(0, "(")
        input_val.append(")")

    list = balance_brackets(input_val)
    print(list)
    # print(last_pair(list))
    print(transform_list(list))

    before = " ".join(list)
    became = " ".join(transform_list(list))
    print("\n--before: ", before, "\nbecame: ", became, "\n")

    result = eval(became)
    print("--result: ", result)
    print("--Ending process...\n")
    return result


def parse_expression(expression):
    # Убрать лишние пробелы по краям и разделить строку по пробелам
    tokens = expression.strip().split()
    return tokens
