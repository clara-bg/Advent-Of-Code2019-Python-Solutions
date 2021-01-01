# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 10:15:27 2021

@author: Clara
"""
from math import floor

with open(r"..\Inputs\01.txt") as file:
    data = file.read().splitlines()

def part_A(data):
    total = 0
    for i in data:
        total += floor(int(i) / 3) - 2      # floor rounds down
    return total

def part_B(data):
    total = 0
    for i in data:
        while True:
            i = floor(int(i) / 3) - 2
            if i <= 0:
                break
            total += i    
    return total

print('Part A: Fuel required =', part_A(data))
print('Part B: Fuel required =', part_B(data))
