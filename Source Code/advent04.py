# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 14:51:11 2021

@author: Clara
"""


lower_limit = 264360
upper_limit = 746325 


def generate_nums(lower_limit, upper_limit):
    all_nums = []
    for i in range(lower_limit, upper_limit):
        all_nums.append(i)
    return all_nums

def check_adjacent_A(element):
    valid = False
    for i in range(5):
        element = str(element)
        if element[i] == element[i + 1]:
            valid = True
    return valid

def check_adjacent_B(element):
    letters = []
    for i in str(element):
        letters.append(i)
    for i in letters:
        if (letters.count(i) == 2):
            return True
    return False

def check_decreasing(element):
    valid = True
    for i in range(1 , 6):
        element = str(element)
        if int(element[i]) < int(element[i - 1]):
            valid = False
            return valid
    return valid

def part_A():
    valid_total = 0
    all_nums = generate_nums(lower_limit, upper_limit)
    for i in all_nums:
        if check_adjacent_A(i) and check_decreasing(i):
            valid_total += 1
    return valid_total

def part_B():
    valid_total = 0
    all_nums = generate_nums(lower_limit, upper_limit)
    for i in all_nums:
        if check_adjacent_B(i) and check_decreasing(i):
            valid_total += 1
    return valid_total


print('Part A: The number of valid passwords is =', part_A())
print('Part B: The number of valid passwords is =', part_B())














    