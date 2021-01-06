# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 07:48:30 2021

@author: Clara
"""

def get_data(_file):
    orbits = {}
    objects = set()
    for line in _file:
        to_orbit, orbiter = line.rstrip().split(")")
        orbits[orbiter] = to_orbit
        objects.add(to_orbit)
        objects.add(orbiter)
    return orbits, objects


def get_orbit(current_obj, orbits):
    if current_obj not in orbits: 
        return []
    return [orbits[current_obj]] + get_orbit(orbits[current_obj], orbits)


def get_total_orbits(orbits):
    return sum(len(get_orbit(obj, orbits)) for obj in objects)


def get_path_between(start, end, orbits):
    start_path, end_path = get_orbit(start, orbits), get_orbit(end, orbits)
    overlapping_point = [i for i in start_path if i in end_path][0] # Gets the first point that is in both paths
    return start_path.index(overlapping_point) + end_path.index(overlapping_point)


with open(r"..\Inputs\06.txt") as _file:
    orbits, objects = get_data(_file)

print("Part 1: The total number of direct and indirect orbits  =", get_total_orbits(orbits))
print('Part 2: The minimum number of orbital transfers required =', get_path_between("YOU", "SAN", orbits))