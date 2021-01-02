# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 08:30:34 2021

@author: Clara
"""

  
data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,6,23,27,1,6,27,31,2,31,9,35,1,35,6,39,1,10,39,43,2,9,43,47,1,5,47,51,2,51,6,55,1,5,55,59,2,13,59,63,1,63,5,67,2,67,13,71,1,71,9,75,1,75,6,79,2,79,6,83,1,83,5,87,2,87,9,91,2,9,91,95,1,5,95,99,2,99,13,103,1,103,5,107,1,2,107,111,1,111,5,0,99,2,14,0,0]

data[1] = 12
data[2] = 2

def my_func(data):
    data = data[:]  # Creates a shallow copy
    for i in range(0, len(data), 4):
        operator = data[i]
        firstnum = data[data[i + 1]]
        secondnum = data[data[i + 2]]
        if operator == 99:
            return data[0]
        elif operator == 1:
            data[data[i + 3]] = firstnum + secondnum
        elif operator == 2:
            data[data[i + 3]] = firstnum * secondnum
    return data[0]

print('Part A: The value at position 0 is =', my_func(data))

for noun in range(100):
    for verb in range(100):
        data[1] = noun
        data[2] = verb
        output = my_func(data)
        if output == 19690720:
            answer = 100 * noun + verb
            print('Part B: 100 * noun + verb =', answer)
            break