# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 19:42:23 2021

@author: Clara
"""

f = open(r"..\..\Inputs\03.txt")
data = f.read()
data = data.splitlines()
f.close()

path_1 = data[0].split(',')
path_2 = data[1].split(',')


def get_pos(path):
    x = 0
    y = 0
    coordinates = []
    for i in path:
        for j in range(int(i[1:])):
            if i[0] == 'R':
                x += 1
            if i[0] == 'L':
                x -= 1
            if i[0] == 'U':
                y += 1
            if i[0] == 'D':
                y -= 1
            coordinates.append([x,y])
    return (coordinates)
    
def manhattan(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    return abs(x) + abs(y)

def convert_to_set(path):
    path_set = [tuple(i) for i in path]
    path_set = set(path_set)
    return path_set

def part_A():
    set_path_1 = convert_to_set(get_pos(path_1))
    set_path_2 = convert_to_set(get_pos(path_2))
    intersections = set_path_1.intersection(set_path_2)
    man_distances = []
    for coordinates in intersections:
        man_distances.append(manhattan(coordinates))
    return min(man_distances)
    
part_A = part_A()
print('Part A: Manhattan distance for closest intersection =', part_A)