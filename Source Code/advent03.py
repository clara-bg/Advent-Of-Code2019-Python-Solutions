# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 10:45:27 2021

@author: Clara
"""


f = open(r"..\Inputs\03.txt")
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
            coordinates.append((x,y))
    return (coordinates)    # returns list of tuples
    
def manhattan(coordinates):
    x = coordinates[0]
    y = coordinates[1]
    return abs(x) + abs(y)

def convert_to_set(path):   # Got this method online because my code didn't want to convert directly from list to set
    path_set = [tuple(i) for i in path]
    path_set = set(path_set)
    return path_set

def main():
    steps = set()
    path_1_coords = get_pos(path_1)
    path_2_coords = get_pos(path_2)
    set_path_1 = convert_to_set(path_1_coords)
    set_path_2 = convert_to_set(path_2_coords)
    intersections = set_path_1.intersection(set_path_2)
    man_distances = []
    for coordinates in intersections:
        man_distances.append(manhattan(coordinates))
        steps.add(path_1_coords.index(coordinates)+ path_2_coords.index(coordinates))
    print('Part A: Manhattan distance for closest intersection =', min(man_distances))
    print('Part B: Minimum number of steps to intersection =', min(steps) + 2) # You have to add 2 here because index starts from 0 but steps should start from 1 and index is called twice.
    
main()