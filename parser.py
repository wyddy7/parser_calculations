import math
from bracket_check import *
from functions import *

def transform_list (list):
    new_list = []
    for i in range(len(list)):
        print("reading: ", list[i])
        if list[i] == "/p/":
            print("sqrt")
            # new_list = sqrt_p(list)
            if not new_list:
                print("New-list is empty")
                new_list = sqrt_p(list)
            else:
                print("New-list is not empty")
                new_list = sqrt_p(new_list)
        elif list[i] == "lg":
            if not new_list:
                print("New-list is empty")
                new_list = lg(list)
            else:
                print("New-list is not empty")
                new_list = lg(new_list)
        elif list[i] == "ln":
            if not new_list:
                print("New-list is empty")
                new_list = ln(list)
            else:
                print("New-list is not empty")
                new_list = ln(new_list)
        elif list[i] == "y^x":
            if not new_list:
                print("New-list is empty")
                new_list = degree_y(list)
            else:
                print("New-list is not empty")
                new_list = degree_y(new_list)
        elif list[i] == "sin" or list[i] == "cos" or list[i] == "tan" or list[i] == "cot":
            if not new_list:
                print("New-list is empty")
                new_list = trigonometr(list)
            else:
                print("New-list is not empty")
                new_list = trigonometr(new_list)

        if new_list is None:  # Проверка на случай, если одна из функций вернула None
            raise ValueError("Одна из функций вернула None. Проверьте реализацию.")
        
        if list[i] == list[len(list)-1] and not new_list:
            new_list = list

    return new_list    
    


def rez(input_val):
    print('Getting new value...')
    if not is_balanced(input_val):  # Проверка на сбалансированность скобок
        input_val.insert(0, '(')
        input_val.append(')')

    
    list = balance_brackets(input_val)
    print(list)
    # print(last_pair(list))
    print(transform_list(list))

    before = " ".join(list)
    became = " ".join(transform_list(list))
    print("before: ", before, "\nbecame: ", became)

    result = eval(became)
    print(result)
    print('Ending process...\n')

def parse_expression(expression):
    # Убрать лишние пробелы по краям и разделить строку по пробелам
    tokens = expression.strip().split()
    return tokens

# TEST

# нужно 3 + 4 * ( ( 7 /p/ 9 * 25 ) lg + 6 = преобразовать в 3  + 4 * lg ( sqrt ( 7 ^ 2 + 9 ^ 2) * 25 + 6) = 
input_val = ['3', '+', '4', '*', '(', '(', '7', '/p/', '9', '*', '25', ')', 'lg', '+', '6']
rez(input_val)

# 3 + 2 * 7 y^x 2 преобразовать в 3 + 2 * 7 ** 2 
input_val = ['3', '+', '2', '*', '7', 'y^x', '2']
rez(input_val)

# 4 * 5 / 7 + 29 / 3 * 11 ) * ( 19 / ( 2 + 4 ) + ( 13 + Pi ) / 4 = преобразовать в ( 4 * 5 / 7 + 29 / 3 * 11 ) * ( 19 / ( 2 + 4 ) + ( 13 + 3,1415926 ) / 4 )

input_val = ['4', '*', '5', '/', '7', '+', '29', '/',  '(', '3', '*', '11', ')', ')', '*', '(', '19', '/', '(', '2', '+', '4', ')', '+', '(', '13', '+', '3.1415926', ')', '/', '4']
rez(input_val)

input_val = parse_expression("4 * 5 / 7 + 29 / ( 3 * 11 ) ) * ( 19 / ( 2 + 4 ) + ( 13 + 3.1415926 ) / 4")
rez(input_val)


# ln
input_val = parse_expression("3 + 4 * ( ( 7 /p/ 9 * 25 ) ln + 6")
rez(input_val)

# sin
input_val = parse_expression("6 sin + ( 6 + 8 ) sin")
rez(input_val)

# cos
input_val = parse_expression("6 cos + ( 6 + 8 ) cos")
rez(input_val)

# tam
input_val = parse_expression("6 tan + ( 6 + 8 ) tan")
rez(input_val)

# cot
input_val = parse_expression("6 cot + ( 6 + 8 ) cot")
rez(input_val)