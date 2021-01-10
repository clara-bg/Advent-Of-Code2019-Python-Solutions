# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 08:33:05 2021

@author: Clara
"""


with open(r"..\Inputs\05.txt") as file:
    data = list(map(int, file.read().split(',')))

def intcode(data, input):
    position = 0
    opcode = 0
    while data[position] != 99:
        opcode, mode = get_mode(data[position]) 
        if opcode == 99:
            print('final', data[0])
        elif opcode == 1:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            dest = data[position+3]
            data[dest] = v1+v2
            position += 4
        elif opcode == 2:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            dest = data[position+3]
            data[dest] = v1*v2
            position += 4
        elif opcode == 3:
            dest = data[position+1]
            data[dest] = input
            position += 2
        elif opcode == 4:
            v1 = get_value(data, position+1, mode[0])
            print('out:', v1)
            position += 2
        elif opcode == 5:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            if v1 != 0:
                position = v2
            else:
                position += 3
        elif opcode == 6:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            if v1 == 0:
                position = v2
            else:
                position += 3
        elif opcode == 7:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            dest = data[position+3]
            data[dest] = int(v1 < v2)
            position += 4
        elif opcode == 8:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            dest = data[position+3]
            data[dest] = int(v1 == v2)
            position += 4
            
def get_mode(first):
    opcode = first % 100
    mode = [int(d) for d in str(first//100)]
    mode = [0] * (3-len(mode)) + mode
    return opcode, mode[::-1]

def get_value(data, position, immediate):
    if immediate:
        return data[position]
    else:
        return data[data[position]]
    
def intcode(data, input):
    position = 0
    opcode = 0
    while data[position] != 99:
        opcode, mode = get_mode(data[position]) 
        if opcode == 99:
            print('final', data[0])
        elif opcode == 1:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            dest = data[position+3]
            data[dest] = v1+v2
            position += 4
        elif opcode == 2:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            dest = data[position+3]
            data[dest] = v1*v2
            position += 4
        elif opcode == 3:
            dest = data[position+1]
            data[dest] = input
            position += 2
        elif opcode == 4:
            v1 = get_value(data, position+1, mode[0])
            print('out:', v1)
            position += 2
        elif opcode == 5:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            if v1 != 0:
                position = v2
            else:
                position += 3
        elif opcode == 6:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            if v1 == 0:
                position = v2
            else:
                position += 3
        elif opcode == 7:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            dest = data[position+3]
            data[dest] = int(v1 < v2)
            position += 4
        elif opcode == 8:
            v1 = get_value(data, position+1, mode[0])
            v2 = get_value(data, position+2, mode[1])
            dest = data[position+3]
            data[dest] = int(v1 == v2)
            position += 4
            
def get_mode(first):
    opcode = first % 100
    mode = [int(d) for d in str(int(first/100))]
    mode = [0] * (3-len(mode)) + mode
    return opcode, mode[::-1]

def get_value(data, position, immediate):
    if immediate:
        return data[position]
    else:
        return data[data[position]]

print('Part A: The diagnostic code =')
intcode(data.copy(), 1)

print('\nPart B: The diagnostic code for system ID 5  =')
intcode(data.copy(), 5)
