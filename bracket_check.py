import math

def count_letters(list, val):
    count = 0
    for item in list:
        if item == '(' == val:
            count += 1
        elif item == ')' == val:
            count += 1
    return count

def is_balanced(text, brackets="〈〉()[]{}"):
    opening, closing = brackets[::2], brackets[1::2]
    stack = []  # keep track of opening brackets types
    for character in text:
        if character in opening:  # bracket
            stack.append(opening.index(character))
        elif character in closing:  # bracket
            if stack and stack[-1] == closing.index(character):
                stack.pop()  # remove the matched pair
            else:
                return False  # unbalanced (no corresponding opening bracket) or
                               # unmatched (different type) closing bracket
    return (not stack)  # no unbalanced brackets

# 3 + 4 * ( ( 7 /p/ 9 * 25 ) 
def last_pair(list):
    if list[len(list)-1] == ')':
        close_bracket_flag = 0
        reversed_list = []
        for item in list[::-1]:
            if item == '(' and close_bracket_flag == 1: 
                reversed_list.append(item)
                # print(1, close_bracket_flag, item)
                return reversed_list[::-1]
            elif item == ')':
                close_bracket_flag += 1
                reversed_list.append(item)
                # print(2, close_bracket_flag, item)
            elif item == '(' and close_bracket_flag > 0:
                close_bracket_flag -= 1
                reversed_list.append(item)
                # print(3, close_bracket_flag, item)
            elif item != '(':
                reversed_list.append(item)
                # print(4, close_bracket_flag, item)
    else: return list[len(list)-1:]

# 9 * 25 ) lg + 6 
def next_pair(list):
    # print("OH NOOOO: ", list[0])
    new_list = []
    if list[0] == '*': list = list[1:]
    if list[0] == '(':
        close_bracket_flag = 0
        for item in list:
            # print("item: ", item)
            if item == ')' and close_bracket_flag == 1: 
                new_list.append(item)
                # print("next_pair is: ", new_list)
                return new_list
            elif item == ')' and close_bracket_flag > 1:
                new_list.append(item)
                close_bracket_flag -= 1
            elif item == '(':
                new_list.append(item)
                close_bracket_flag += 1
            else:
                new_list.append(item)
                # print(2, close_bracket_flag, item)
    else:
        new_list.append(list[0])
        return new_list



def balance_brackets (list):
    open_brackets = count_letters(list, '(')
    close_brackets = count_letters(list, ')')
    difference = open_brackets - close_brackets
    # print('dif: ', difference)
    if difference > 0:
        while difference != 0:
            list.append(')')
            difference -= 1
    elif difference < 0:
        while difference != 0:
            list.insert(0, '(')
            difference += 1


    return list