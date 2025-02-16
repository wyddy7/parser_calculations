from bracket_check import *
import re

def sqrt_p (list):
    # print('found sqrt_p...')
    for i in range(len(list)):
        if list[i] == "/p/":
            pair = last_pair(list[:i])
            first_args = list[:i - len(pair)]   
            second_args = list[i+1:]
            pair_two = next_pair(second_args)
            # print(first_args, " and ", second_args)

            # new_list = first_args + ["sqrt", "("] + pair + ["**", "2", "+"] + pair_two + ["**", "2", ")"] + second_args[len(pair_two):]
            new_list = first_args
            new_list.append("math.sqrt")
            new_list.append("(")
            new_list += pair
            new_list.append('**')
            new_list.append('2')
            new_list.append('+')
            new_list += pair_two
            new_list.append('**')
            new_list.append('2')
            new_list.append(')')
            new_list += second_args[len(pair_two):]
            # print("new_list: ", new_list)
            return new_list
        
def lg(list):
    # print('found log10...')
    # print("WTF IS HERE???")
    for i in range(len(list)):
        if list[i] == "lg":
            pair = last_pair(list[:i])
            # print("pair:", pair)
            first_args = list[:i - len(pair)]   
            second_args = list[i+1:]
            # print(first_args, " and2 ", second_args)

            new_list = first_args
            new_list.append("math.log10")
            new_list.append("(")
            new_list += pair
            new_list.append(")")
            new_list += second_args
            return new_list
        
def trigonometr(list):
    for i in range(len(list)):
        if list[i] == "sin" or list[i] == "cos" or list[i] == "tan" or list[i] == "cot":
            # print(f'found {list[i]}...')
            pair = last_pair(list[:i])
            # print("pair:", pair)
            first_args = list[:i - len(pair)]   
            second_args = list[i+1:]
            # print(first_args, " and2 ", second_args)
            # print(list[i])
            new_list = first_args
            if list[i] == "sin": new_list.append("math.sin")
            elif list[i] == "cos": new_list.append("math.cos")
            elif list[i] == "tan": new_list.append("math.tan")
            new_list.append("(")
            new_list += pair
            new_list.append(")")
            new_list += second_args
            return new_list
        
def ln(list):
    for i in range(len(list)):
        if list[i] == "ln":
            pair = last_pair(list[:i])
            # print("pair:", pair)
            first_args = list[:i - len(pair)]   
            second_args = list[i+1:]
            # print(first_args, " and2 ", second_args)

            new_list = first_args
            new_list.append("math.log")
            new_list.append("(")
            new_list += pair
            new_list.append(")")
            new_list += second_args
            # print(new_list)
            return new_list

def degree_y(list):
    for i in range(len(list)):
        if list[i] == "y^x":
            pair = last_pair(list[:i])
            # print("pair:", pair)
            first_args = list[:i - len(pair)]   
            second_args = list[i+1:]
            pair_two = next_pair(second_args)
            
            # print(first_args, " and2 ", second_args)

            new_list = first_args
            new_list.append("(")
            new_list += pair
            new_list.append("**")
            new_list += pair_two
            new_list.append(")")
            # print('pair_two len: ', len(pair_two))
            new_list += second_args[len(pair_two):]
            return new_list
def reverse_x(list):
    print("list:", list)
    addition = []
    new_list = []
    for i in range(len(list)):
        if list[i] == "1/":
            pair = last_pair(list[:i])
            print("pair:", pair)
            first_args = list[:i - len(pair)]   
            previous_val = [first_args[len(first_args)-1]]
            print('previous_val:', previous_val, re.match(r'^-?\d+(\.\d+)?$', previous_val[0]))
            if previous_val[0] not in {'-', '+', '*', '/', ')' , '('} and not re.match(r'^-?\d+(\.\d+)?$', previous_val[0]): 
                addition = previous_val
                print('addition:', addition)
            second_args = list[i+1:]
            
            # print(first_args, " and2 ", second_args)

            new_list = first_args
            if addition: 
                new_list.pop()
            new_list.append("(")
            new_list.append("1")
            new_list.append("/")
            if addition: 
                new_list += addition
            new_list += pair
            new_list.append(")")
            new_list += second_args
            
    return new_list
