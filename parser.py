import math
from bracket_check import *
from functions import *


def transform_listy(listy: list):
    if not listy:
        return []
    new_listy = []
    operations = {
        "/p/": sqrt_p,
        "sqrt": sqrt,
        "lg": lg,
        "ln": ln,
        "y^x": degree_y,
        "sin": trigonometr,
        "cos": trigonometr,
        "tan": trigonometr,
        "1/": reverse_x,
    }

    for item in listy:
        if item in operations:
            func = operations[item]
            new_listy = func(new_listy if new_listy else listy)

            if new_listy is None:
                raise ValueError("Одна из функций вернула None. Проверьте реализацию.")
            if item == listy[len(listy) - 1] and not new_listy:
                new_listy = listy

    return new_listy if new_listy else listy


def rez(input_val: list):
    print("--Getting new value...")
    if not is_balanced(input_val):  # Проверка на сбалансированность скобок
        input_val.insert(0, "(")
        input_val.append(")")

    listy = balance_brackets(input_val)
    print(listy)
    # print(last_pair(listy))
    print(transform_listy(listy))

    before = " ".join(listy)
    became = " ".join(transform_listy(listy))
    print("\n--before: ", before, "\n--became: ", became, "\n")

    result = eval(became)
    print("--result: ", result)
    print("--Ending process...\n")
    return result


def parse_expression(expression: list):
    # Убрать лишние пробелы по краям и разделить строку по пробелам
    tokens = expression.strip().split()
    return tokens
