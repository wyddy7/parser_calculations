import math


def count_letters(listy: list, val: str):
    count = 0
    for item in listy:
        if item == "(" == val:
            count += 1
        elif item == ")" == val:
            count += 1
    return count


def is_balanced(text: list, brackets="〈〉()[]{}"):
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
    return not stack  # no unbalanced brackets


# 3 + 4 * ( ( 7 /p/ 9 * 25 )
def last_pair(listy: list):
    if listy[len(listy) - 1] == ")":
        close_bracket_flag = 0
        reversed_listy = []
        for item in listy[::-1]:
            if item == "(" and close_bracket_flag == 1:
                reversed_listy.append(item)
                # print(1, close_bracket_flag, item)
                return reversed_listy[::-1]
            elif item == ")":
                close_bracket_flag += 1
                reversed_listy.append(item)
                # print(2, close_bracket_flag, item)
            elif item == "(" and close_bracket_flag > 0:
                close_bracket_flag -= 1
                reversed_listy.append(item)
                # print(3, close_bracket_flag, item)
            elif item != "(":
                reversed_listy.append(item)
                # print(4, close_bracket_flag, item)
    else:
        return listy[len(listy) - 1 :]


# 9 * 25 ) lg + 6
def next_pair(listy: list):
    # print("OH NOOOO: ", listy[0])
    new_listy = []
    if listy[0] == "*":
        listy = listy[1:]
    if listy[0] == "(":
        close_bracket_flag = 0
        for item in listy:
            # print("item: ", item)
            if item == ")" and close_bracket_flag == 1:
                new_listy.append(item)
                # print("next_pair is: ", new_listy)
                return new_listy
            elif item == ")" and close_bracket_flag > 1:
                new_listy.append(item)
                close_bracket_flag -= 1
            elif item == "(":
                new_listy.append(item)
                close_bracket_flag += 1
            else:
                new_listy.append(item)
                # print(2, close_bracket_flag, item)
    else:
        new_listy.append(listy[0])
        return new_listy


def balance_brackets(listy: list):
    open_brackets = count_letters(listy, "(")
    close_brackets = count_letters(listy, ")")
    difference = open_brackets - close_brackets
    # print('dif: ', difference)
    if difference > 0:
        while difference != 0:
            listy.append(")")
            difference -= 1
    elif difference < 0:
        while difference != 0:
            listy.insert(0, "(")
            difference += 1

    return listy
